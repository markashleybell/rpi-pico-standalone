# Hardware

- [Raspberry Pi Pico W](https://shop.pimoroni.com/products/raspberry-pi-pico-w?variant=40059369619539)
- [Pimoroni LiPo SHIM for Pico](https://shop.pimoroni.com/products/pico-lipo-shim?variant=32369543086163)
- [2200mAh Lithium Ion Battery Pack](https://shop.pimoroni.com/products/lithium-ion-battery-pack?variant=23417820359)

# Notes

This project is developed using [Visual Studio Code](https://code.visualstudio.com/) and the [Pico-W-Go](https://github.com/paulober/Pico-W-Go) extension.

**Gotcha**: The Pico-W-Go extension settings are a bit confusing, and **Upload Project** _seems_ to entirely ignore the project sync folder(s) and file ignore settings. 

So currently, if you use the **Upload Project** option it just uploads absolutely everything to the Pi... including the `.vscode` folder, which is then undeleteable without [nuking the flash memory](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html#resetting-flash-memory).

For now it's best to just use the individual file upload option, until this gets fixed—or I work out it's actually me doing something wrong in the settings!
