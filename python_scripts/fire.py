# From NeoPixel library 
# Authors: Max Kolanz, Jonah Embry, and Griffin Malm

import time

from neopixel import *


# LED strip configuration:
LED_COUNT      = 99      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

from random import *


def fireRandom():
        """Draw rainbow that uniformly distributes itself across all pixels."""
#the increment and the A1-H8 define the possible colors the pixels can be
	increment = 20
        A1 = Color(255, 0, 0)
        B2 = Color(255, increment, 0)
        C3 = Color(255, increment * 2, 0)
        D4 = Color(255, increment * 3, 0)
        E5 = Color(255, increment * 4, 0)
        F6 = Color(255, increment * 5, 0)
        G7 = Color(255, increment * 6, 0)
        H8 = Color(255, increment * 7, 0)
#the for loop with i and the number of pixels cycles through all the pixels we have so that they each get called when a random number does
        for i in range (strip.numPixels()):
                threeQuarters = randrange(0, 4)
                if threeQuarters == 1 or threeQuarters == 2 or threeQuarters == 3 :
#the above if statement and the threeQuarters variable makes it so that the pixels only recieve a color 75% of the time. This makes a flicker.
                        shade = randrange(0,9)

                        if shade == 1:
                                strip.setPixelColor(i, A1)
                                strip.show()
                        elif shade == 2:
                                strip.setPixelColor(i, B2)
                                strip.show()
                        elif shade == 3:
                                strip.setPixelColor(i, C3)
                                strip.show()
                        elif shade == 4:
                                strip.setPixelColor(i, D4)
                                strip.show()
                        elif shade == 5:
                                strip.setPixelColor(i, E5)
                                strip.show()
                        elif shade == 6:
                                strip.setPixelColor(i, F6)
                                strip.show()
                        elif shade == 7:
                                strip.setPixelColor(i, G7)
				strip.show()
			else: 
				strip.setPixelColor(i, H8)
				strip.show()
# above is connected to shade which is a random integer between one and 9. each one coresponds to a color listed above and the
# pixels are randomly changed to be one of the 9 fire related colors.


# Main program logic follows:
if __name__ == '__main__':
        # Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        # Intialize the library (must be called once before other functions).
        strip.begin()

        print ('Press Ctrl-C to quit.')
        while True:
 
fireRandom()