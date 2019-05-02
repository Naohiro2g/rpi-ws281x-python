https://dordnung.de/raspberrypi-ledstrip/ws2812
http://www.neko.ne.jp/~freewing/raspberry_pi/raspberry_pi_gpio_pwm_ws2812b_rgb_led/




## Wiring


WS2812  |  RPi
|-------|-------|
GND     |  GND
DIN     |  GPIO18 or 12
VDC     |  3.3V or 5V
GND     |  GND

The module says "4-7VDC" but it works at both 3.3V or 5V of RasPi.

## Test drive

You need to be the super user. Set -c to clear the display on exit. 
LED_PIN=18, LED_COUNT=16 for 2 units, brightness is 64/255 which is bright enough.

```
sudo python3 examples/strandtest.py -c
```

# RPi WS281x Python

This is the official Python distribution of the ws281x library: http://github.com/richardghirst/rpi_ws281x

# Installing

## From pip

Most users should simply run:

```
sudo pip install rpi_ws281x
```
