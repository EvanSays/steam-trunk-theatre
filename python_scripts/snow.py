import time 
import random 
from neopixel import *


# LED strip configuration:
LED_COUNT      = 100      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/sp$
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor l$
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

from random import *
def snowy():
	W1 = Color(50, 50, 50)
	W2 = Color(75, 75, 75)
	W3 = Color(100,100, 100)
	W4 = Color(125, 125, 125)
	W5 = Color(150, 150, 150)

	for i in range(strip.numPixels()):
		threeQuarters = randrange(4)
		if threeQuarters == 1 or threeQuarters == 2 or threeQuarters == 3 :
			shade = randrange(6)

			if shade == 1:
				strip.setPixelColor(i, W1)
				strip.show()
			if shade == 2:
				strip.setPixelColor(i, W2)
				strip.show()
			if shade == 3:
				strip.setPixelColor(i, W4)
				strip.show()
			if shade == 4:
				strip.setPixelColor(i, W5)
			else:
				strip.setPixelColor(i, W3)

	
def snowy2 ():

	red = 100
	rstep = 100.0
	green = 100
	gstep = 100.0
	blue = 100
	bstep = 100.0
	which = randrange(20)
	time.sleep(0.75)

	if which == 2:
		for j in range(32):

			entrance = Color(red, green, blue)
			for i in range(40):
				strip.setPixelColor(i, entrance)
			rstep -= 1.563
			red = int(round(rstep))
			gstep -= 1.563
			green = int(round(gstep))
			bstep -= 1.563
			blue = int(round(bstep))
			strip.show()
			time.sleep(0.1)
	else:
		red = 50
		rstep= 50.0
		green = 50
		gstep = 50.0
		blue = 50
		bstep = 50.0

		for j in range(32):
			entrance = Color(red, green, blue)

			for i in range(40):
				strip.setPixelColor(i, entrance)
			rstep += 1.563
			red = int(round(rstep))
			gstep += 1.563
			green = int(round(gstep))
			bstep += 1.563
			blue = int(round(bstep))
			strip.show()
			time.sleep(0.1)

	if which == 4:
		red2 = 100
		rstep2 = 100.0
		green2 = 100
		gstep2 = 100.0
		blue2 = 100
		bstep2 = 100.0
		for j in range(32):
		
			entrance = Color(red, green, blue)
			for i in range(40, 95):
				strip.setPixelColor(i, entrance)
			rstep2 += 1.563
			red2 = int(round(rstep))
			gstep2 += 1.563
			green2 = int(round(gstep))
			bstep2 += 1.563
			blue2 = int(round(bstep))
			strip.show()
			time.sleep(0.1)
	else:
		red2 = 150
		rstep2 = 150.0
		green2 = 150
		gstep2 = 150.0
		blue2 = 150
		bstep2 = 150.0
		
		for j in range(32):
			entrance = Color(red2, green2, blue2)

			for i in range(40, 95):
				strip.setPixelColor(i, entrance)
			rstep2 -= 1.563
			red2 = int(round(rstep2))
			gstep2 -= 1.563
			green2 = int(round(gstep2))
			bstep2 -= 1.563
			blue2 = int(round(bstep2))

	sky = Color(100, 100, 100)

	for i in range(96):
		strip.setPixelColor(i, sky)
	strip.show()

if __name__ == '__main__':
        # Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        # Intialize the library (must be called once before other functions).
        strip.begin()

        print ('Press Ctrl-C to quit.')

	while True:

                snowy()

