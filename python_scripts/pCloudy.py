#Right now the cloud deletes the sun which is not good.

import time
from neopixel import *
import random

LED_COUNT       = 96
LED_PIN         = 18
LED_FREQ_HZ     = 800000
LED_DMA         = 5
LED_BRIGHTNESS  = 255
LED_INVERT      = False
LED_CHANNEL     = 0
LED_STRIP       = ws.WS2811_STRIP_GRB

def cloudCycle(strip):
        sky = Color(20, 20, 215)
        black = Color(0, 0, 0)

        for i in range(0, 95, 1):
                if (i % 2 == 0):
                        strip.setPixelColor(i, sky)
                else:
                        strip.setPixelColor(i, black)

        strip.show()

	time.sleep(0.5)
#def dayCycle(strip,wait_ms=1):

        count = 0
        for i in range(0, 61, 1):
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
                if (count < 38):
                        strip.setPixelColor(95-i, sun1)
                if (count == 8 or count == 9):
                        strip.setPixelColor(95-i, sun2)
                if (count == 6 or count == 7):
                        strip.setPixelColor(95-i, sun4)
                if (count == 4 or count == 5):
                        strip.setPixelColor(95-i, sun4)
                if (count == 3):
                        strip.setPixelColor(95-i, sun5)
                if (count == 2):
                         strip.setPixelColor(95-i, sun6)
                if (count == 1):
                         strip.setPixelColor(95-i, sun7)
                if (count == 0):
                        strip.setPixelColor(95-i, sun8)
                if(count % 2 == 0):
                        strip.setPixelColor(95-i+6, black)
                else:
                        strip.setPixelColor(95-i+6, sky)

                #Forward Mid and Front Right
                if(17 < count < 55):
                        strip.setPixelColor(2+i, sun1)
                if(count == 45 or count == 46):
                        strip.setPixelColor(2+i, sun2)
                if(count == 47 or count == 48):
                        strip.setPixelColor(2+i, sun3)
                if(count == 49 or count == 50):
                        strip.setPixelColor(2+i, sun4)
                if(count == 51):
                        strip.setPixelColor(2+i, sun5)
                if(count == 52):
                        strip.setPixelColor(2+i, sun6)
                if(count == 53):
                        strip.setPixelColor(2+i, sun7)
                if(count == 54):
                        strip.setPixelColor(2+i, sun8)
                if(count % 2 == 0):
                        strip.setPixelColor(2+i-6, sky)
                else:
                        strip.setPixelColor(2+i-6, black)
                #Back Mid
                if(17 < count < 41):
                        strip.setPixelColor(37-i, sun1)
                if(count % 2 == 0):
                        strip.setPixelColor(37-i+6, black)
                else:
                        strip.setPixelColor(37-i+6, sky)

		#Moving Clouds

		if(17 <count < 41):
			cloud = random.randint(0, 4)
			if cloud == 1:					#Sets it so clouds randomly pass
				cloudy = Color(0, 255, 0)		#Cloud Color
				for k in range(0, 25, 1):
					if k  < 20:
						print "1"
						strip.setPixelColor(k, cloudy)
			                	strip.setPixelColor(39-k, cloudy)	
					if(k % 2 == 0):
                       				 print "2"
						 strip.setPixelColor(k-4, black)
						 strip.setPixelColor(43-k, sky)
                			else:
                        			 print "3"
						 strip.setPixelColor(k-4, sky)
						 strip.setPixelColor(43-k, black)
					strip.show()
					time.sleep(0.2)



                count += 1
                strip.show()
                time.sleep(.5)



if __name__ == '__main__':
        # Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel (LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        # Intialize the library (must be called once before other functions).
        strip.begin()

        print('Press Ctrl-C to quit.')
#        entrance(strip)
        while True:
#                sky(strip)
		cloudCycle(strip)

