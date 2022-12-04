from machine import ADC, Pin

charging = Pin('WL_GPIO2', Pin.IN)

full_battery = 3.85
empty_battery = 3.0

class PowerMonitor:
    def __init__(self, wlan):
        self.wlan = wlan

    def get_vsys(self):
        conversion_factor = 3 * 3.3 / 65535

        try:
            # Don't use the WLAN chip for a moment.
            self.wlan.active(False)

            # Make sure pin 25 is high.
            Pin(25, mode=Pin.OUT, pull=Pin.PULL_DOWN).high()
            
            # Reconfigure pin 29 as an input.
            Pin(29, Pin.IN)
            
            vsys = ADC(29)
            return vsys.read_u16() * conversion_factor

        finally:
            # Restore the pin state and possibly reactivate WLAN
            Pin(29, Pin.ALT, pull=Pin.PULL_DOWN, alt=7)
            self.wlan.active(True)

    def status(self):
        # convert the raw ADC read into a voltage, and then a percentage
        voltage = self.get_vsys()

        percentage = 100 * ((voltage - empty_battery) / (full_battery - empty_battery))

        if percentage > 100:
            percentage = 100.00

        status = "Charging" if charging.value() == 1 else "Battery"

        return (status, '{:.2f}'.format(voltage) + "v", '{:.0f}%'.format(percentage))
