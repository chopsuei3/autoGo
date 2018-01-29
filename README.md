# autoGo

This code allows you to control the button a Pokemon Go Plus accessory with an Arduino, and also incorporates 2 scripts which allow the Plus to stay connected indefinitely.
The code was developed on Ubuntu 14.04 LTS using an Arduino Nano and an Omron G6D-1A relay. The Arduino wiring diagram can be found below.

## Setup
To test, my setup consisted of 
- Ubuntu 14.04 LTS laptop
- Android 6.0.1 device with USB debugged enabled, connected to the computer above
- Arduino Nano wired to the Pokemon Go Plus with an Omron G6D-1A relay to simulate the button press

Important Notes
- USB debugging must be enabled and computer must be trusted
- Android display should be set to "always on"
- Timing of the vibrations was off sometimes, so counts of caught vs fled may be incorrect, but it should still function regardless

## go_plus_control.ino
This script is meant to be loaded on to an Arduino Uno or Nano with the appropriate settings for the device.
The Arduino wiring diagram will be added shortly.


## go_plus_daemon.py
This script is run from the computer (e.g. Ubuntu) and will perform the following tasks - 
- check Pokemon Go Plus icon status on the screen using adb
- if the Plus is disconnected, the button the Plus will be pushed and an input tap on the Plus icon will be sent to the device via adb
- Vibration times will be measured and translated into events such as "Pokemon caught" or "Pokemon not caught"
- Prints a summary every 10 minutes of the total # of reconnects, pokemon caught, and pokemon fled


## check_plus_icon.sh
This script is run by the python script above to check the status (color) of the Pokemon Go Plus icon on the screen.




### References and sources
This project was inspired by, and uses code from /u/c00ni on reddit to run the Arudino, so all credit and thanks to them for this.

[Link to c00ni's reddit thread](https://www.reddit.com/r/GoPlus/comments/7pribw/go_plus_modded_for_auto_press_via_arduino/)