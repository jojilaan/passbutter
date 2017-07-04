# import libraries
import RPi.GPIO as GPIO
import time

class Romp(object):

		def __init__(self):
				GPIO.setmode(GPIO.BCM)          #set the GPIO on BCM
				GPIO.setup(20, GPIO.OUT)	#Step
				GPIO.setup(21, GPIO.OUT)	#Dir
				GPIO.setup(16, GPIO.OUT)	#_EN
				self.pwm = GPIO.PWM(20, 100)	#set pin 20 to PWM			
				self.pwm.start(0)               #start pwm
		
		def Buigen(self, hoek):
				GPIO.output(16, GPIO.LOW)       #set pin 16 to LOW
				time.sleep(0.1)                 #wait 0.1 seconds
				self.pwm.ChangeDutyCycle(20)    
				time.sleep(0.1 * hoek)          #wait 0.1 seconds
				GPIO.output(16, GPIO.HIGH)      #set pin 16 to HIGH
		
		def cleanUp(self):
				GPIO.cleanup(20)                #remove any states on pin 20
				GPIO.cleanup(21)                #remove any states on pin 21
				GPIO.cleanup(16)                #remove any states on pin 16
