import time
from neopixel import *

LED_COUNT       = 100
LED_PIN         = 18
LED_FREQ_HZ     = 800000
LED_DMA         = 5
LED_BRIGHTNESS  = 255
LED_INVERT      = False
LED_CHANNEL     = 0
LED_STRIP       = ws.WS2811_STRIP_GRB

def dayCycle(strip):

	sky = Color(20, 20, 215)
	black = Color(0, 0, 0)

	for i in range(95):
                if (i % 2 == 0):
			strip.setPixelColor(i, sky)
		else:
			strip.setPixelColor(i, black)

        strip.show()

#Create sun that moves across the sky, which is darker/more red at the ends.
#def dayCycle(strip):
	time.sleep(0.5)

        for i in range(61):
                # Lower sun number means lighter color.
		sun1 = Color(255, 255, 100)
		sun2 = Color(255, 255, 26)
                sun3 = Color(255, 204, 0)
		sun4 = Color(255, 140, 26)
		sun5 = Color(255, 102, 0)
		sun6 = Color(255, 71, 26)
		sun7 = Color(255, 51, 0)
                sun8 = Color(255, 26, 26)
                sky = Color(20, 20, 215)
                black = Color(0, 0, 0)

		#Front Left and Front Top
		if (i <= 37):
			strip.setPixelColor(94-i, sun1)
			if (i == 8 or i == 9):
                        	strip.setPixelColor(94-i, sun2)
			if (i == 6 or i == 7):
                        	strip.setPixelColor(94-i, sun4)
			if (i == 4 or i == 5):
                        	strip.setPixelColor(94-i, sun4)
			if (i == 3):
                        	strip.setPixelColor(94-i, sun5)
			if (i == 2):
				strip.setPixelColor(94-i, sun6)
			if (i == 1):
                        	strip.setPixelColor(94-i, sun7)
			if (i == 0):
                        	strip.setPixelColor(94-i, sun8)
			if(i % 2 == 0):
                       		strip.setPixelColor(94-i+6, black)
                	else:
                        	strip.setPixelColor(94-i+6, sky)

		#Middle Front and Front Right
		if(17 <= i <= 53):
                        strip.setPixelColor(3+i, sun1)
			if(i == 45 or i == 46):
                        	strip.setPixelColor(3+i, sun2)
			if(i == 47 or i == 48):
                        	strip.setPixelColor(3+i, sun3)
			if(i == 49 or i == 50):
                        	strip.setPixelColor(3+i, sun4)
			if(i == 51):
                        	strip.setPixelColor(3+i, sun5)
			if(i == 52):
                        	strip.setPixelColor(3+i, sun6)
			if(i == 53):
                        	strip.setPixelColor(3+i, sun7)
			if(i == 54):
                        	strip.setPixelColor(3+i, sun8)
			if(i % 2 == 0):
                        	strip.setPixelColor(3+i-6, black)
                	else:
                        	strip.setPixelColor(3+i-6, sky)

		#Middle Back
                if(17 <= i <= 36):
               		strip.setPixelColor(36-i, sun1)
                	if(i % 2 == 0):
               			strip.setPixelColor(36-i+6, black)
               		else:
                       		strip.setPixelColor(36-i+6, sky)

                strip.show()
                time.sleep(0.25)

if __name__ == '__main__':
        # Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel (LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        # Intialize the library (must be called once before other functions).
	strip.begin()

	print('Press Ctrl-C to quit.')
        while True:
#		dayTime(strip)
		dayCycle(strip)
		
