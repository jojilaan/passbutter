# import libraries
import RPi.GPIO as GPIO
import time

class Romp(object):

		def __init__(self):
				GPIO.setmode(GPIO.BCM)
				GPIO.setup(20, GPIO.OUT)	#Step
				GPIO.setup(21, GPIO.OUT)	#Dir
				GPIO.setup(16, GPIO.OUT)	#_EN
				
		def Buigen(self, hoek):
				GPIO.output(16, GPIO.LOW)
				time.sleep(0.1)
				for x in range (0, (hoek*100)):
					GPIO.output(20, True)
					time.sleep(0.000008)
					GPIO.output(20, False)
					time.sleep(0.000008)
				GPIO.output(16, GPIO.HIGH)
					
if __name__ == "__main__":
		romp = Romp()
		hoek = 90
		romp.Buigen(hoek)
		
