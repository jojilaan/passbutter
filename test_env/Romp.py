# import libraries
import RPi.GPIO as GPIO
import time

class Romp(object):

		def __init__(self):
				GPIO.setmode(GPIO.BCM)
				GPIO.setup(20, GPIO.OUT)	#Step
				GPIO.setup(21, GPIO.OUT)	#Dir
				GPIO.setup(16, GPIO.OUT)	#_EN
				self.pwm = GPIO.PWM(20, 100)				
				self.pwm.start(0)
		
		def Buigen(self, hoek):
				GPIO.output(16, GPIO.LOW)
				time.sleep(0.1)
				self.pwm.ChangeDutyCycle(20)
				time.sleep(0.1 * hoek)
				GPIO.output(16, GPIO.HIGH)
		
		def cleanUp(self):
				GPIO.cleanup(20)
				GPIO.cleanup(21)
				GPIO.cleanup(16)
if __name__ == "__main__":
		romp = Romp()
		hoek = 90
		romp.Buigen(hoek)
		romp.cleanUp()		
