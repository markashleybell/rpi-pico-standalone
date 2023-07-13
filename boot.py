import network
import rp2
import time

from config import SSID, PASSWORD

# Set country (this influences WLAN channels)
rp2.country('GB')

# Disable access point interface
ap = network.WLAN(network.AP_IF)
ap.active(False)

# Enable station interface
wlan = network.WLAN(network.STA_IF)
# Optionaly disable power saving mode
# wlan.config(txpower=0xa11140)
wlan.active(True)

wlan.connect(SSID, PASSWORD)

retries = 10

while retries > 0 and wlan.status() != network.STAT_GOT_IP:
    retries -= 1
    time.sleep(1)

if wlan.status() != network.STAT_GOT_IP:
    raise RuntimeError('Network connection failed')
