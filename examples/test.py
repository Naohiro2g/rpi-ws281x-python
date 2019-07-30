#!/usr/bin/env python3

from rpi_ws281x import *
from  strandtest import colorWipe, theaterChase, rainbow, rainbowCycle, theaterChaseRainbow
import time
import argparse

# Process command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
parser.add_argument('-b', '--brightness', type=int, default=20, help='brightness 0 to 255')
parser.add_argument('-p', '--pixel_count', type=int, default=8, help='how many pixels?')
args = parser.parse_args()


# LED strip configuration:
LED_COUNT      = args.pixel_count  # Number of LED pixels.
LED_PIN        = 18                # GPIO pin connected to the pixels (12/18:pwm0, 13/19:pwm1).
#LED_PIN        = 10               # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000            # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10                # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = args.brightness   # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False             # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0                 # set to '1' for GPIOs 13, 19, 41, 45 or 53


# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

print ('Press Ctrl-C to quit.')
if not args.clear:
    print('(hint: Use "-c" command line argument to clear LEDs on exit)')


print(strip.numPixels(), "pixels")
strip.setPixelColor(0, Color(64, 0, 0))
strip.setPixelColor(1, Color(0, 64, 0))
strip.setPixelColor(2, Color(0, 0, 255))
strip.setPixelColor(3, Color(64, 64, 255))
strip.setPixelColor(4, Color(255, 255, 255))
strip.show()

input("press enter to continue")


try:
    print('colorWipe')
    colorWipe(strip, Color(255, 0, 0), 100)  # Red wipe
    colorWipe(strip, Color(255, 255, 0), 20)  # Purple wipe
    colorWipe(strip, Color(0, 255, 0), 20)  # Blue wipe
    colorWipe(strip, Color(0, 255, 255), 20)  # Cyan wipe
    colorWipe(strip, Color(0, 0, 255))  # Green wipe
    colorWipe(strip, Color(255, 0, 255))  # Yellow wipe

    print('theaterChase')
    theaterChase(strip, Color(127, 127, 127))  # White theater chase
    theaterChase(strip, Color(127,   0,   0))  # Red theater chase
    theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
    print('theaterChaseRainbow')
    theaterChaseRainbow(strip, wait_ms=25)

    print('rainbow')
    rainbow(strip, iterations=3)
    print('rainbowCycle')
    rainbowCycle(strip, iterations=3)

except KeyboardInterrupt:
    if args.clear:
        print('clear to finish')
        colorWipe(strip, Color(0,0,0), 50)

print('finish!  hint: Use "-c" command line argument to clear LEDs on exit')
