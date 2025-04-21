from boot import wlan
from machine import Pin
from microdot import Microdot, send_file
from power import PowerMonitor

led = Pin("LED", Pin.OUT)
led.value(0)

if (wlan.isconnected()):
    led.value(1)

power_monitor = PowerMonitor(wlan)

app = Microdot()

@app.route('/')
async def index(request):
    return send_file('index.html', content_type='text/html')

@app.route('/led')
async def toggle_led(request):
    val = led.value() == 0
    led.value(val)
    return { 'status': 'ON' if val else 'OFF' }

@app.route('/pwr')
async def get_power_status(request):
    status, voltage, charge = power_monitor.status()
    return { 'status': status, 'voltage': voltage, 'charge': charge }

# TODO: https://github.com/miguelgrinberg/microdot/tree/main/examples/tls

app.run(debug=True)
