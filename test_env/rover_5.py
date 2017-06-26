# import libraries
import RPi.GPIO as GPIO
import time
class Rover(object):
		
		def __init__(self):
				
				GPIO.setmode(GPIO.BCM)
				GPIO.setup(11, GPIO.OUT)					#Pwm LEFT        
				GPIO.setup(9, GPIO.OUT)				#Dir LEFT
				self.pwm_L = GPIO.PWM(11, 100)

				GPIO.setup(8, GPIO.OUT)				#Pwm Right        
				GPIO.setup(25, GPIO.OUT)					#Dir Right
				self.pwm_R = GPIO.PWM(8, 100)
				
				self.pwm_L.start(0)
				self.pwm_R.start(0)

		def goForward(self, speed, t):
				self.speed = speed
				GPIO.output(9, GPIO.HIGH)
				GPIO.output(25, GPIO.LOW)
				self.pwm_L.ChangeDutyCycle(self.speed)
				self.pwm_R.ChangeDutyCycle(self.speed)
				time.sleep(t)

		def goBackward(self, speed, t):
				self.speed = speed
				GPIO.output(9, GPIO.LOW)
				GPIO.output(25, GPIO.HIGH)
				self.pwm_L.ChangeDutyCycle(self.speed)
				self.pwm_R.ChangeDutyCycle(self.speed)
				time.sleep(t)

		def stopRover(self):
				self.speed = 0
				self.pwm_L.ChangeDutyCycle(0)
				self.pwm_R.ChangeDutyCycle(0)
		
		def turnRover(self, direction, speed, t):
				self.speed = speed
				if(direction == "right"):
						GPIO.output(9, GPIO.LOW)
						GPIO.output(25, GPIO.LOW)
				else:
						GPIO.output(9, GPIO.HIGH)
						GPIO.output(25, GPIO.HIGH)
				self.pwm_L.ChangeDutyCycle(self.speed)
				self.pwm_R.ChangeDutyCycle(self.speed)
				time.sleep(t)

		def cleanUp(self):
				GPIO.cleanup(9)
				GPIO.cleanup(11)
				GPIO.cleanup(25)
				GPIO.cleanup(8)
		
		def getSpeed(self):
				return self.speed
		

if __name__ == '__main__':
		rover = Rover()
		rover.turnRover("left",28, 2.2)
		rover.stopRover()
		rover.cleanUp()
