import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)	#Step
GPIO.setup(21, GPIO.OUT)	#dir

GPIO.output(21, False)

for x in range (0, 30000):
		GPIO.output(20, True)
		GPIO.output(20, False)
		time.sleep(0.0001)
