#http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
#answers.opencv.org/question/23450/countig-blue-pixels-in-image-python/
#stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python

from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import numpy as np

class Camera(object):
                def __init__(self):
                    self.cap = PiCamera()
                    self.cap.resolution = (320, 240)
                    self.cap.framerate = 15
                    self.rawCapture = PiRGBArray(self.cap, size=(320, 240))
                    self.cap.vflip = True
                    self.cap.hflip = True
                    time.sleep(0.1)

                def herkenBoter(self, kleur):
                    for frame in self.cap.capture_continuous(self.rawCapture, format="rgb", use_video_port=True):
                        image = frame.array
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        image = image[90:240,149:169]

                        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

                        if kleur == "geel":
                            lower_yellow = np.array([20,100,100])
                            upper_yellow = np.array([40,255,255])

                            mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

                            res = cv2.bitwise_and(image, image, mask= mask)

                            aantal_kleur = cv2.countNonZero(mask)
                        else:
                            lower_blauw = np.array([110,50,50])
                            upper_blauw = np.array([130,255,255])

                            mask = cv2.inRange(hsv, lower_blauw, upper_blauw)

                            res = cv2.bitwise_and(image, image, mask= mask)

                            aantal_kleur = cv2.countNonZero(mask)

                        self.rawCapture.truncate(0)
                        return aantal_kleur
