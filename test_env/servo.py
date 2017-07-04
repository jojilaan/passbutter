import RPi.GPIO as GPIO
import time

class Arm:

		def __init__(self):
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(19, GPIO.OUT)
			GPIO.setup(26, GPIO.OUT)
			self.pwm_l = GPIO.PWM(19,50)
			self.pwm_r = GPIO.PWM(26,50)
			self.pwm_l.start(0)
			self.pwm_r.start(0)


		def updateAngle(self, kleur):
		        if kleur == "geel":
                            self.pwm_l.ChangeDutyCycle(10.0)
			    time.sleep(1)
			    self.pwm_r.ChangeDutyCycle(4.0)
			    time.sleep(1)
                        else:
                            self.pwm_r.ChangeDutyCycle(10.0)
			    time.sleep(1)
			    self.pwm_l.ChangeDutyCycle(4.0)
			    time.sleep(1)
		
		def cleanUp(self):
			GPIO.cleanup(19)
			GPIO.cleanup(26)
