#Written by Max Kolanz, Jonah Embry, and Griffin Malm

import time
from neopixel import *

LED_COUNT	= 95
LED_PIN		= 18
LED_FREQ_HZ	= 800000
LED_DMA		= 5
LED_BRIGHTNESS	= 255
LED_INVERT	= False
LED_CHANNEL	= 0
LED_STRIP	= ws.WS2811_STRIP_GRB
#This is the necessary stuff to set up the strips

def dayTime(strip, wait_ms=1):

        sky_W = Color(100, 100, 200) #more white of a sky
        sky_B = Color(60, 60, 255) #more blue of a sky

        for i in range(0, 20): #Selects Middle Back 
                strip.setPixelColor(i, sky_W)
                strip.show()
	for i in range(20, 40):#Selects Middle Forward
		strip.setPixelColor(i, sky_B)
		strip.show()
	for i in range(58, 78):#Selects Front Top
		strip.setPixelColor(i, sky_B)
		strip.show()
        for i in range(78, 96):#Selects Front Left
                strip.setPixelColor(i, sky_W)
		strip.show()
	for i in range(40, 58):#Selects Front Right
		strip.setPixelColor(i, sky_W)
                strip.show()
#The above function selects the range of pixels and applies two shades of sky to them

if __name__ == '__main__':
        strip = Adafruit_NeoPixel (LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        strip.begin()
#The while true makes it run continuously because it never isn't true.
        print('Press Ctrl-C to quit.')
        while True:
                dayTime(strip)
                time.sleep(300)

