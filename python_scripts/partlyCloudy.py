#Authors: Max Kolanz, Jonah Embry, Griffin Malm

import time
from neopixel import *

LED_COUNT       = 96
LED_PIN         = 18
LED_FREQ_HZ     = 800000
LED_DMA         = 5
LED_BRIGHTNESS  = 255
LED_INVERT      = False
LED_CHANNEL     = 0
LED_STRIP       = ws.WS2811_STRIP_GRB

from random import *

def day():
	"""Sets the pixels on the top of the box to the blue sky color"""
	sunnySky = Color(60, 60, 255)

	for i in range(40):
		strip.setPixelColor(i, sunnySky)
	for i in range(58, 76):
		strip.setPixelColor(i, sunnySky)
	strip.show()

	time.sleep(0.5)
#def cloudy():
	"""Allows the clouds to pass randomly accross the sky based on cloud variable"""
	sunnySky = Color(60, 60, 255)
	cloud_color = Color(40, 40, 90)
	cloud = randrange(0, 20)
	sleep_value = randrange(0, 10)
#the values that make the colors of the sky and the variable then makes a cloud move overhead


	if cloud == 1:#determines if a cloud is called

		for j in range (40):
			#used to count across pixels
			if j <= 19:
				#in the lower have of the range 40
				#if uses equations based on j to select pixels
				strip.setPixelColor(j, cloud_color)
				strip.setPixelColor(39 - j, cloud_color)
				strip.setPixelColor(58 + j, cloud_color)
				time.sleep(0.33)
			if j >= 19:#upper half of j moves sky back across
				strip.setPixelColor(j - 19, sunnySky)
				strip.setPixelColor(58 - j, sunnySky)
				strip.setPixelColor(39 + j, sunnySky)
				time.sleep(0.33)
			strip.show()
		time.sleep(sleep_value)		


#It is set so the random number determines if the cloud will pass or not. 
#right now it just flashes the cloud color can you use the daycycle to make it work here?

	strip.show()



if __name__ == '__main__':
        # Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel (LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        # Intialize the library (must be called once before other f$
        strip.begin()

        print('Press Ctrl-C to quit.')

        while True:
		day()

