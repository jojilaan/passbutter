import threading
from rover_5 import Rover
from UltrasoneSensor import UltrasoneSensor
from KleurenSensor import KleurenSensor
from Camera import Camera
from servo import Arm
import time
import RPi.GPIO as GPIO
from multiprocessing.pool import ThreadPool

class Robot(object):
		
		def RijNaarBoter(self):				
				t1.daemon = True
				t3.daemon = True
				t4.daemon = True
				t1.start()
				t3.start()
				t4.start()

				bool = True

				while bool:
						USS_voor_result = pool1.apply_async(USS.MeetAfstandVoor)
						return_USS_Voor = USS_voor_result.get()
						kleur_result = pool2.apply_async(kleurensensor.isBlack)
						return_kleur = kleur_result.get()
						print return_USS_Voor
						print return_kleur
						if return_USS_Voor <= 15 or return_kleur == True:
								rover.stopRover()
								bool = False


		def DraaiRobot(self):
				rover.turnRover('left', 58, 6.4)

				rover.stopRover()

				arm = Arm()
				arm.updateAngle()

		def ZoekBoter(self, camera):
                                while True:
                                    return_camera = camera.herkenBoter("geel")
                                    time.sleep(1)
                                    print return_camera
                                    if return_camera > 10:
                                        break
                                    else:
                                        rover.turnRover('left', 58, 0.1)
                                        rover.stopRover()

				rover.stopRover()

		def RijNaarBord(self):
				t7.daemon = True

				t7.start()
				bool = True

				while bool:
						USS_voor_result = pool1.apply_async(USS.MeetAfstandVoor)
						return_USS_Voor = USS_voor_result.get()
						kleur_result = pool2.apply_async(kleurensensor.isBlack)
						return_kleur = kleur_result.get()
						print return_USS_Voor
						print return_kleur
						if return_USS_Voor <= 15 or return_kleur == True:
								rover.stopRover()
								bool = False

                def ZoekBord(self, camera):
                                while True:
                                    return_camera = camera.herkenBoter("blauw")
                                    time.sleep(1)
                                    print return_camera
                                    if return_camera > 10:
                                        break
                                    else:
                                        rover.turnRover('left', 58, 0.1)
                                        rover.stopRover()

				rover.stopRover()




if __name__ == '__main__':
		GPIO.setmode(GPIO.BCM)
		rover = Rover()
		USS = UltrasoneSensor()
		kleurensensor = KleurenSensor()
		camera = Camera()
		robot = Robot()

		speed = 28
		direction = 'left'
		speed2 = 50
		t = 2

		t1 = threading.Thread(target=USS.MeetAfstandVoor)
		t2 = threading.Thread(target=USS.MeetAfstandAchter)
		t3 = threading.Thread(target=kleurensensor.isBlack)
		t4 = threading.Thread(target=rover.goForward, args=(speed,))
		t5 = threading.Thread(target=rover.turnRover, args=(direction, speed2, t))
		t6 = threading.Thread(target=rover.goBackward, args=(speed,))		
		t7 = threading.Thread(target=rover.goForward, args=(speed,))

		pool1 = ThreadPool(processes=1)
		pool2 = ThreadPool(processes=2)
		pool3 = ThreadPool(processes=3)

		robot.ZoekBoter(camera)
		robot.RijNaarBoter()
		robot.DraaiRobot()
		robot.ZoekBord(camera)
		robot.RijNaarBord()
		GPIO.cleanup()
