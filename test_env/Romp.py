# import libraries
import RPi.GPIO as GPIO
import time

class Romp(object):

		def __init__(self)
				GPIO.setmode(GPIO.BCM)
				GPIO.setup(21, GPIO.OUT)
				
		def Buigen(hoek)
				for x in rangen (0, (hoek*100))
					GPIO.output(21, True)
					time.sleep(0.000008)
					GPIO.output(21, False)
					time.sleep(0.000008)
					
if __name__ = "__main__"
		romp = Romp()
		hoek = 90
		romp.Buigen(hoek)
		