
from flask import Flask, render_template, request
app = Flask(__name__)

from random import *

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



@app.route("/")
class main(object):

	myFunctions = { "Off" : True, "Fire" : False}

		
	def off1(self):

    		import off

		off.turnoff(strip)

		if __name__ == '__main__':
		
        	# Create NeoPixel object with appropriate configuration.
			strip = Adafruit_NeoPixel (LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        		# Intialize the library (must be called once before other f$
        		strip.begin()

        		print('Press Ctrl-C to quit.')

        		while True:
				
				turnoff(strip)
				for k in myFunctions:
					
					templateData = {
						myFucntions : k
						}
				# Pass the template data into the template main.html and return it to the user
				return render_template('main.html', **templateData)

	def fire1(self):
		import time

		import fire
		
		fire.fireRandom()

		# Main program logic follows:
		if __name__ == '__main__':
			# Create NeoPixel object with appropriate configuration.
			strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        		# Intialize the library (must be called once before other functions).
        		strip.begin()

        		print ('Press Ctrl-C to quit.')
        		while True:
 
				fireRandom()
		
				for k in myFunctions:
					templateData = {
        	        	        myFunctions : k
        	        	        }
				# Pass the template data into the template main.html and return it to the user
        	        	return render_template('main.html', **templateData)


	# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<action>")
def action(action):

	# If the action part of the URL is "on," execute the code indented below:
	for k in myFunctions:
		
		if action == "on":
			# Set the boolean to true:
			myFunctions[k] = True
			# Save the status message to be passed into the template

		if action == "off":
			myFunctions[k] = False
		
		if action == "toggle":
			# Read the pin and set it to whate
			if myFunctions[k] == True:
				myFunctions[k] == False
			else:
				myFunctions[k] == True

		   # Along with the pin dictionary, put the message into the template data dictionary:
		templateData = {
		      myFunctions : k 
		}
		return render_template('main.html', **templateData)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
	while True:
		m = main()
	while myFunctions["Off"] == True:
                m.off1()
        while myFunctions["Fire"] == False:
                m.fire1()
