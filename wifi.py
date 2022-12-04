import network
import time

def connect(ssid, password, logger):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        logger('Waiting for connection...')
        time.sleep(1)

    if wlan.status() != 3:
        raise RuntimeError('Network connection failed')
    else:
        logger('Connected')
        status = wlan.ifconfig()
        logger('IP address: ' + status[0])

    return wlan
