# import sensor from library
# code from: github.com/adafruit/adafruit_python_tcs34725/blob/master/examples/simpletest.py
import time
import smbus
class KleurenSensor(object):
        def __init__(self):
                self.bus = smbus.SMBus(1)
                self.bus.write_byte(0x29, 0x80|0x12)
                self.ver = bus.read_byte(0x29)
                if (self.ver == 68):
                        print("Device found\n")
                        self.bus.write_byte(0x29, 0x80|0x00)
                        self.bus.write_byte(0x29, 0x01|0x02)
                        self.bus.write_byte(0x29, 0x80|0x14)
        def isBlack(self):
                self.data = self.bus.read_i2c_block_data(0x29, 0)
                self.red = self.data[3] << 8 | self.data[2]
                self.green = self.data[5] << 8 | self.data[4]
                self.blue = self.data[7] << 8 | self.data[6]
                self.red = self.red / 256 
                self.green = self.green / 256 
                self.blue = self.blue / 256
                print('R: {0}   G: {1}    B: {2}'.format(self.red, self.green, self.blue))
                if (self.red < 30 and self.green < 30 and self.blue < 30):
                        return True
                else:
                        return False
