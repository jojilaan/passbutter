from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import numpy as np

cap = PiCamera()
cap.resolution = (320, 240)
cap.framerate = 30
rawCapture = PiRGBArray(cap, size=(320, 240))
cap.vflip = True
time.sleep(0.1)

for frame in cap.capture_continuous(rawCapture, format="rgb", use_video_port=True):
		image = frame.array
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

		lower_yellow = np.array([20,100,100])
		upper_yellow = np.array([40,255,255])

		mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

		res = cv2.bitwise_and(image, image, mask= mask)

		cv2.imshow("geel", res)

		cv2.imshow("Frame", image)
		key = cv2.waitKey(1) & 0XFF

		rawCapture.truncate(0)

		if key == ord("q"):
				break
