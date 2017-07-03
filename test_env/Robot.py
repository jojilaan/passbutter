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
				#t1 = threading.Thread(target=USS.MeetAfstandVoor)
				#t2 = threading.Thread(target=kleurensensor.isBlack)
				#t3 = threading.Thread(target=rover.goForward, args=(speed,))
				t1.daemon = True
				t3.daemon = True
				t4.daemon = True
				t1.start()
				t3.start()
				t4.start()

				#pool1 = ThreadPool(processes=1)
				#pool3 = ThreadPool(processes=2)

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
				#GPIO.cleanup()
				#t1._stop()
				#t3._stop()
				#t4._stop()
				#GPIO.cleanup()

		def DraaiRobot(self):
				#t4 = threading.Thread(target=rover.turnRover, args=())
				#t5 = threading.Thread(target=USS.MeetAfstandAchter)
				#t2.daemon = True
				
				#t5.start()
				rover.turnRover('left', 58, 6.4)
				#time.sleep(15)
				#t6.start()
				rover.stopRover()
				#bool = True

				#while bool:
				#		USS_achter_result = pool1.apply_async(USS.MeetAfstandAchter)
				#		return_USS_Achter = USS_achter_result.get()
						#kleur_result = pool2.apply_async(kleurensensor.isBlack)
				#		if return_USS_Achter <= 13:
				#				rover.stopRover()
				#				bool = False
				#t2._stop()
				#t5.stop()
				#t6.stop()
				arm = Arm()
				arm.updateAngle()

		def ZoekBoter(self, camera):
				#t4 = threading.Thread(target=rover.turnRover, args=())
				#t5 = threading.Thread(target=USS.MeetAfstandAchter)
				#t7.daemon = True
				#t7.start()
				#camera_result = pool1.apply_async(camera.herkenBoter)
				#return_camera = camera_result.get()
				#t5.start()
                                while True:
                                    return_camera = camera.herkenBoter("geel")
                                    time.sleep(1)
                                    print return_camera
                                    if return_camera > 10:
                                        break
                                    else:
                                        rover.turnRover('left', 58, 0.1)
                                        rover.stopRover()

                                
				#time.sleep(15)
				#t6.start()
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
				#t4 = threading.Thread(target=rover.turnRover, args=())
				#t5 = threading.Thread(target=USS.MeetAfstandAchter)
				#t7.daemon = True
				#t7.start()
				#camera_result = pool1.apply_async(camera.herkenBoter)
				#return_camera = camera_result.get()
				#t5.start()
                                while True:
                                    return_camera = camera.herkenBoter("blauw")
                                    time.sleep(1)
                                    print return_camera
                                    if return_camera > 10:
                                        break
                                    else:
                                        rover.turnRover('left', 58, 0.1)
                                        rover.stopRover()

                                
				#time.sleep(15)
				#t6.start()
				rover.stopRover()




if __name__ == '__main__':
		GPIO.setmode(GPIO.BCM)
		rover = Rover()
		USS = UltrasoneSensor()
		kleurensensor = KleurenSensor()
		camera = Camera()
		robot = Robot()
		#camera = Camera()
		speed = 28
		direction = 'left'
		speed2 = 50
		t = 2
		#RijNaarBoter(speed)
		#robot.RijNaarBoter()
		t1 = threading.Thread(target=USS.MeetAfstandVoor)
		t2 = threading.Thread(target=USS.MeetAfstandAchter)
		t3 = threading.Thread(target=kleurensensor.isBlack)
		t4 = threading.Thread(target=rover.goForward, args=(speed,))
		t5 = threading.Thread(target=rover.turnRover, args=(direction, speed2, t))
		t6 = threading.Thread(target=rover.goBackward, args=(speed,))
		
		t7 = threading.Thread(target=rover.goForward, args=(speed,))
		#t7 = threading.Thread(target=camera.herkenBoter)
		'''t1.start()
		
		t5 = threading.Thread(target=rover.turnRover, args=())
		t1.start()
		t2.start()
		t3.start()
		t4.start()
		#print "Main complete"
		'''
		pool1 = ThreadPool(processes=1)
		pool2 = ThreadPool(processes=2)
		pool3 = ThreadPool(processes=3)
		#pool7 = ThreadPool(processes=7)

		#USS_voor_result = pool1.apply_async(USS.MeetAfstandVoor)
		#USS_achter_result = pool2.apply_async(USS.MeetAfstandAchter)
		#kleur_result = pool3.apply_async(kleurensensor.isBlack)
		robot.ZoekBoter(camera)
		robot.RijNaarBoter()
		robot.DraaiRobot()
		robot.ZoekBord(camera)
		robot.RijNaarBord()
		GPIO.cleanup()
						
		'''
		bool = True

		while bool:
				async_result = pool1.apply_async(USS.MeetAfstandVoor)
				return_val = async_result.get()
				kleur_result = pool3.apply_async(kleurensensor.isBlack)
				return_kleur = kleur_result.get()
				print return_kleur
				print return_val
				if return_val <= 10 and not return_val == "None" or return_kleur == True:
						rover.stopRover()
						bool = False
        #time.sleep(0.5)
    
		#time.sleep(10)
		GPIO.cleanup()'''
