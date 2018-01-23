import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

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
class main():

	myOff = {
		'state' : True,
		}
	myfire = {
		'state' : Flase,
		}
	for key in myOff:

		while myOff[key]==True:
		
			def off1():

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
	
				templateData = {
					'title' : 'Lights are off!',
      					}
				# Pass the template data into the template main.html and return it to the user
				return render_template('main.html', **templateData)
	for key in myfire: 

		while myfire[key] == True:

			def fire1():
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
		
	
				templateData = {
        	        	        'title' : 'Lights are off!',
        	        	        }
        	        	# Pass the template data into the template main.html and return it to the user
        	        	return render_template('main.html', **templateData)


# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = booleans[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the boolean to true:
      ['state'] = True
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      booleans['state'] = False
      message = "Turned " + deviceName + " off."
   if action == "toggle":
      # Read the pin and set it to whatever it isn't (that is, toggle it):
      if booleans['state'] == True:
		booleans['state'] = False
      else:
		booleans['state'] = True
      message = "Toggled " + deviceName + "."


   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'message' : message,
      'booleans' : booleans
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
