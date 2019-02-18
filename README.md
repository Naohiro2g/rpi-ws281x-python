## Wiring

======  ======
WS2812  RPi
======  ======
GND     GND
DIN     GPIO18
VDC     3.3V
GND     GND
======  ======

## Test drive

You need to be a super user. Set -c to clear the display on exit.

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
