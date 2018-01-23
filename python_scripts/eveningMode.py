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

def eveningTime(strip, wait_ms=1):

        sky_B = Color(25, 25, 12) #more blue of a sky
        sky_P = Color(75, 0, 130) #more purple of a sky
	#Colors for the setting sun
        sun1 = Color(255, 255, 100)
        sun2 = Color(255, 255, 26)
        sun3 = Color(255, 204, 0)
        sun4 = Color(255, 140, 26)
        sun5 = Color(255, 102, 0)
        sun6 = Color(255, 71, 26)
        sun7 = Color(255, 51, 0)
        sun8 = Color(255, 26, 26)


        for i in range(0, 20, 2): #Selects Middle Back
                strip.setPixelColor(i, sky_B)
                strip.show()
        for i in range(20, 40, 2):#Selects Middle Forward
                strip.setPixelColor(i, sky_B)
                strip.show()
        for i in range(58, 78, 2):#Selects Front Top
                strip.setPixelColor(i, sky_P)
                strip.show()
        for i in range(78, 90):#Selects Front Left
                strip.setPixelColor(i, sky_P)
                strip.show()
        for i in range(46, 58):#Selects Front Right
                strip.setPixelColor(i, sky_P)
                strip.show()
#Sets the Pixels for the sun colors on both sides of the box
	strip.setPixelColor(91, sun8)
	strip.setPixelColor(90, sun7)
	strip.setPixelColor(89, sun6)
	strip.setPixelColor(88, sun5)
	strip.setPixelColor(87, sun4)
	strip.setPixelColor(86, sun3)
	strip.setPixelColor(85, sun2)
	strip.setPixelColor(84, sun1)
	strip.setPixelColor(56, sun8)
	strip.setPixelColor(55, sun7)
	strip.setPixelColor(54, sun6)
	strip.setPixelColor(53, sun5)
	strip.setPixelColor(52, sun4)
	strip.setPixelColor(51, sun3)
	strip.setPixelColor(50, sun2)	
	strip.setPixelColor(49, sun1)
	strip.show()

#The above function selects the range of pixels and applies two shades of sky to them
if __name__ == '__main__':
        strip = Adafruit_NeoPixel (LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        strip.begin()
#The while true makes it run continuously because it never isn't true.
        print('Press Ctrl-C to quit.')
        while True:
                eveningTime(strip)
                time.sleep(300)
