
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

def lightning():
	"""Makes a dark and stormy sky and sometimes flashes a bit with lightning"""
        sky = Color(50, 50, 255)
        lightFlash = Color(255, 255, 255)
        flashChance = randrange(10)#the chance the lightning goes off
        Black = Color(0, 0, 0)

	time = 0
        for i in range(40):
                strip.setPixelColor(i, sky)

        for i in range(58, 76):
                strip.setPixelColor(i, sky)
                strip.show()
        #Sets the Pixels on the Top of the Box to a dark sky color
        for i in range(40, 58):
                strip.setPixelColor(i, Black)

        for i in range(76, 92):
                strip.setPixelColor(i, Black)
                strip.show()
        #Makes the side strips black
        for i in range(58, 97):
                if flashChance == 5:
                        strip.setPixelColor(i, lightFlash)
                        strip.show()
	for i in range(58):
		if flashChance == 5:
			strip.setPixelColor(i, lightFlash)
	strip.show()

        #Makes all the pixels flash with white as i cycles through the strips
	strip.show()

if __name__ == '__main__':
        # Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel (LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        # Intialize the library (must be called once before other f$
        strip.begin()

        print('Press Ctrl-C to quit.')

        while True:
                lightning()



