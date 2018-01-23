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

def turnOff(strip):
        off = Color(0, 0, 0)

        for i in range(strip.numPixels()):
                strip.setPixelColor(i, off)
        strip.show()

