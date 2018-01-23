#Written by Max Kolanz, Jonah Embry, and Griffin Malm

import time
from neopixel import *

LED_COUNT       = 95
LED_PIN         = 18
LED_FREQ_HZ     = 800000
LED_DMA         = 5
LED_BRIGHTNESS  = 255
LED_INVERT      = False
LED_CHANNEL     = 0
LED_STRIP       = ws.WS2811_STRIP_GRB
#This is the necessary stuff to set up the strips

def green(strip):
	red = Color(255, 0, 0)
	blue = Color(0, 0, 255)
	green = Color(0, 255, 0)
	purple = Color(255, 0, 255)
	yellow = Color(0, 255, 255)
	orange = Color(255, 255, 0)

	for i in range(strip.numPixels()):
		strip.setPixelColor(i, green)
	strip.show()

def red(strip):
        red = Color(255, 0, 0)
        blue = Color(0, 0, 255)
        green = Color(0, 255, 0)
        purple = Color(255, 0, 255)
        yellow = Color(0, 255, 255)
        orange = Color(255, 255, 0)

        for i in range(strip.numPixels()):
                strip.setPixelColor(i, red)
        strip.show()

def blue(strip):
        red = Color(255, 0, 0)
        blue = Color(0, 0, 255)
        green = Color(0, 255, 0)
        purple = Color(255, 0, 255)
        yellow = Color(0, 255, 255)
        orange = Color(255, 255, 0)

        for i in range(strip.numPixels()):
                strip.setPixelColor(i, blue)
        strip.show()

def purple(strip):
        red = Color(255, 0, 0)
        blue = Color(0, 0, 255)
        green = Color(0, 255, 0)
        purple = Color(255, 0, 255)
        yellow = Color(0, 255, 255)
        orange = Color(255, 255, 0)

        for i in range(strip.numPixels()):
                strip.setPixelColor(i, purple)
        strip.show()

def yellow(strip):
        red = Color(255, 0, 0)
        blue = Color(0, 0, 255)
        green = Color(0, 255, 0)
        purple = Color(255, 0, 255)
        yellow = Color(0, 255, 255)
        orange = Color(255, 255, 0)

        for i in range(strip.numPixels()):
                strip.setPixelColor(i, green)
        strip.show()

def orange(strip):
        red = Color(255, 0, 0)
        blue = Color(0, 0, 255)
        green = Color(0, 255, 0)
        purple = Color(255, 0, 255)
        yellow = Color(255, 255, 0)
        orange = Color(255, 165, 0)

        for i in range(strip.numPixels()):
                strip.setPixelColor(i, green)
        strip.show()


if __name__ == '__main__':
        strip = Adafruit_NeoPixel (LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        strip.begin()
#The while true makes it run continuously because it never isn't true.
        print('Press Ctrl-C to quit.')
        while True:
                green(strip)
