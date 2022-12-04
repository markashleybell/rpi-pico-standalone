from config import SSID, PASSWORD
from power import PowerMonitor
from machine import Pin
from microdot import Microdot, send_file
from wifi import connect

wlan = connect(SSID, PASSWORD, print)

led = Pin("LED", Pin.OUT)
led.value(0)

power_monitor = PowerMonitor(wlan)

app = Microdot()

@app.route('/')
def hello(request):
    return send_file('/index.html', content_type='text/html')

@app.route('/led')
def toggle_led(request):
    val = led.value() == 0
    led.value(val)
    return { 'status': 'ON' if val else 'OFF' }

@app.route('/pwr')
def get_power_status(request):
    status, voltage, charge = power_monitor.status()
    return { 'status': status, 'voltage': voltage, 'charge': charge }

app.run(debug=True)
