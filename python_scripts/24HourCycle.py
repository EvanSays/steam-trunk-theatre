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


def fullCycle(strip):

	#Transition from black to day (used at beginning of program)
#	def entrance(strip):
		red = 0
		rstep = 0.0
		green = 0
		gstep = 0.0
		blue = 0
		bstep = 0.0
	
		for j in range(0, 32, 1):
			entrance = Color(red, green, blue)

			for i in range(0, 95, 1):
				if (i % 2 == 0):
					strip.setPixelColor(i, entrance)

			rstep += 0.625
			red = int(round(rstep))
			gstep += 0.625
			green = int(round(gstep))
			bstep += 6.71875
			blue = int(round(bstep))
	
			strip.show()
        		time.sleep(0.1)
	
		sky = Color(20, 20, 215)
		black = Color(0, 0, 0)

		for i in range(0, 95, 1):
                	if (i % 2 == 0):
				strip.setPixelColor(i, sky)
			else:
				strip.setPixelColor(i, black)
	
        	strip.show()

	#Create sun that moves across the sky, which is darker/more red at the ends.
#	def dayCycle(strip):

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
			if (i < 38):
				strip.setPixelColor(93-i, sun1)
			if (i == 8 or i == 9):
                        	strip.setPixelColor(93-i, sun2)
			if (i == 6 or i == 7):
                       		strip.setPixelColor(93-i, sun4)
			if (i == 4 or i == 5):
                        	strip.setPixelColor(93-i, sun4)
			if (i == 3):
                        	strip.setPixelColor(93-i, sun5)
			if (i == 2):
				strip.setPixelColor(93-i, sun6)
			if (i == 1):
                         	strip.setPixelColor(93-i, sun7)
			if (i == 0):
                        	strip.setPixelColor(93-i, sun8)
                	if(i % 2 == 0):
                        	strip.setPixelColor(93-i+6, black)
                	else:
                        	strip.setPixelColor(95-i+6, sky)

			#Forward Mid and Front Right
			if(17 < i < 55):
                        	strip.setPixelColor(2+i, sun1)
			if(i == 45 or i == 46):
                        	strip.setPixelColor(2+i, sun2)
			if(i == 47 or i == 48):
                        	strip.setPixelColor(2+i, sun3)
			if(i == 49 or i == 50):
                        	strip.setPixelColor(2+i, sun4)
			if(i == 51):
                        	strip.setPixelColor(2+i, sun5)
			if(i == 52):
                        	strip.setPixelColor(2+i, sun6)
			if(i == 53):
                        	strip.setPixelColor(2+i, sun7)
			if(i == 54):
                        	strip.setPixelColor(2+i, sun8)
			if(i % 2 == 0):
                        	strip.setPixelColor(2+i-6, sky)
                	else:
                        	strip.setPixelColor(2+i-6, black)

			#Back Mid
                	if(17 < i < 41):
                		strip.setPixelColor(37-i, sun1)
                	if(i % 2 == 0):
                		strip.setPixelColor(37-i+6, black)
                	else:
                        	strip.setPixelColor(37-i+6, sky)

                	strip.show()
                	time.sleep(0.5)

	#Transition from day to night
#	def dusk(strip):

        	# RGB for day to night transition
		red1 = 20
		r1step = 20.0
		green1 = 20
		g1step = 20.0
		blue1 = 215
		b1step = 215.0

		# RGB values for day to black transition
		red2 = 20
		r2step = 20.0
		green2 = 20
		g2step = 20.0
		blue2 = 215
		b2step = 215.0

		# RGB values for black to night transition
		red3 = 0
		r3step = 0.0
		green3 = 0
		g3step = 0.0
		blue3 = 0
		b3step = 0.0
	
		# Second value is amount of stages in the transitions (in this case 32)
        	for j in range(0, 32, 1):
	
                	dayToNight = Color(red1, green1, blue1)
			dayToBlack = Color(red2, green2, blue2)
			blackToNight = Color(red3, green3, blue3)
	
                	for i in range(0, 95, 1):
				if (i % 2 == 0):
					if (i % 3 == 0):
						strip.setPixelColor(i, dayToNight)
					else:
						strip.setPixelColor(i, dayToBlack)
                        	elif (i % 3 == 0):
					if (i % 2 != 0):
						strip.setPixelColor(i, blackToNight)

			# In order to find amount to increment by, divide difference...
                	# ... in RGB values by total number of stages
			r1step += 1.8125
			red1 = int(round(r1step))
			g1step -= 0.5
			green1 = int(round(g1step))
			b1step -= 2.65625
			blue1 = int(round(b1step))

			r2step -= 0.625
			red2 = int(round(r2step))
			g2step -= 0.625
			green2 = int(round(g2step))
			b2step -= 6.71875
			blue2 = int(round(b2step))
	
			r3step += 2.4375
			red3 = int(round(r3step))
			g3step += 0.125
			green3 = int(round(g3step))
			b3step += 4.0625
			blue3 = int(round(b3step))
	
                	strip.show()
                	time.sleep(0.1)

		sky = Color(78, 4, 130)
		black = Color(0, 0, 0)

		for i in range(0, 95, 1):
                	if (i % 3 == 0):
				strip.setPixelColor(i, sky)
			else:
				strip.setPixelColor(i, black)

        	strip.show()

	#Create moon that moves across the sky.
#	def nightCycle(strip):

        	for i in range(0, 61, 1):
                	moon = Color(255, 255, 40)
                	sky = Color(78, 4, 130)
			black = Color(0, 0, 0)


			#Front Left and Front Top
                	if (i < 38):
                        	strip.setPixelColor(95-i, moon)
                		if(i % 3 == 0):
                        		strip.setPixelColor(95-i+4, sky)
                		else:
                        		strip.setPixelColor(95-i+4, black)

			#Forward Mid and Front Right
                	if(i > 17):
                        	if(i < 55):
                                	strip.setPixelColor(2+i, moon)
                		if(i % 3 == 0):
                        		strip.setPixelColor(2+i-4, sky)
                		else:
                        		strip.setPixelColor(2+i-4, black)

			#Back Mid
                	if(i > 17):
                        	if(i < 41):
                                	strip.setPixelColor(37-i, moon)
                		if(i % 3 == 0):
                        		strip.setPixelColor(37-i+4, sky)
                		else:
                        		strip.setPixelColor(37-i+4, black)

                	strip.show()
			time.sleep(0.5)

	#Transition from night to day
#	def dawn(strip):

        	# RGB for night to day transition
		red1 = 78
		r1step = 78.0
		green1 = 4
		g1step = 4.0
		blue1 = 130
		b1step = 130.0

		# RGB values for black to day transition
		red2 = 0
		r2step = 0.0
		green2 = 0
		g2step = 0.0
		blue2 = 0
		b2step = 0.0

		# RGB values for night to black transition
		red3 = 78
		r3step = 78.0
		green3 = 4
		g3step = 4.0
		blue3 = 130
		b3step = 130.0

		# Second value is amount of stages in the transitions (in this case 32)
        	for j in range(0, 32, 1):

                	nightToDay = Color(red1, green1, blue1)
			blackToDay = Color(red2, green2, blue2)
			nightToBlack = Color(red3, green3, blue3)

                	for i in range(0, 95, 1):
				if (i % 2 == 0):
					if (i % 3 == 0):
						strip.setPixelColor(i, nightToDay)
					else:
						strip.setPixelColor(i, blackToDay)
                        	elif (i % 3 == 0):
					if (i % 2 != 0):
						strip.setPixelColor(i, nightToBlack)

			# In order to find amount to increment by, divide difference...
                	# ... in RGB values by total number of stages
			r1step -= 1.8125
			red1 = int(round(r1step))
			g1step += 0.5
			green1 = int(round(g1step))
			b1step += 2.65625
			blue1 = int(round(b1step))

			r2step += 0.625
			red2 = int(round(r2step))
			g2step += 0.625
			green2 = int(round(g2step))
			b2step += 6.71875
			blue2 = int(round(b2step))

			r3step -= 2.4375
			red3 = int(round(r3step))
			g3step -= 0.125
			green3 = int(round(g3step))
			b3step -= 4.0625
			blue3 = int(round(b3step))

                	strip.show()
                	time.sleep(0.1)
	
		sky = Color(20, 20, 215)
		black = Color(0, 0, 0)

		for i in range(0, 95, 1):
                	if (i % 2 == 0):
				strip.setPixelColor(i, sky)
			else:
				strip.setPixelColor(i, black)
	
        	strip.show()

if __name__ == '__main__':
        # Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel (LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        # Intialize the library (must be called once before other functions).
	strip.begin()

        print('Press Ctrl-C to quit.')
	#entrance(strip)
        while True:
#		dayCycle(strip)
#		dusk(strip)
#		time.sleep(1)
#		nightCycle(strip)
#		dawn(strip)
#		time.sleep(1)
		fullCycle(strip)
