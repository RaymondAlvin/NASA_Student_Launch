# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_bno055
import RPi.GPIO as GPIO
import digitalio
import logging
import sys

'''
i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)
'''


'''
led1 = digitalio.DigitalInOut(board.D4)
led2 = digitalio.DigitalInOut(board.D17)
led3 = digitalio.DigitalInOut(board.D27)
led4 = digitalio.DigitalInOut(board.D22)
'''
led1 = digitalio.DigitalInOut(board.D5)
led2 = digitalio.DigitalInOut(board.D6)
led3 = digitalio.DigitalInOut(board.D13)
led4 = digitalio.DigitalInOut(board.D19)

led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
led3.direction = digitalio.Direction.OUTPUT
led4.direction = digitalio.Direction.OUTPUT

ControlPin = [led1, led2, led3, led4]


seq = [ [True,False,False,False],
        [True,False,False,False],
        [True,False,False,False],
        [False,True,False,False],
        [False,True,False,False],
        [False,True,False,False],
        [False,False,True,False],
        [False,False,True,False] ]




last_val = 0xFFFF

'''
def temperature():
	global last_val  
	result = sensor.temperature
	if abs(result - last_val) == 128:
		result = sensor.temperature
		if abs(result - last_val) == 128:
			return 0b00111111 & result
	last_val = result
	return result
'''

from Adafruit_BNO055 import BNO055


# Create and configure the BNO sensor connection.  Make sure only ONE of the
# below 'bno = ...' lines is uncommented:
# Raspberry Pi configuration with serial UART and RST connected to GPIO 18:
bno = BNO055.BNO055(serial_port='/dev/serial0', rst=18)
# BeagleBone Black configuration with default I2C connection (SCL=P9_19, SDA=P9_20),
# and RST connected to pin P9_12:
#bno = BNO055.BNO055(rst='P9_12')


# Enable verbose debug logging if -v is passed as a parameter.
if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
    logging.basicConfig(level=logging.DEBUG)

# Initialize the BNO055 and stop if something went wrong.
if not bno.begin():
    raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

# Print system status and self test result.
status, self_test, error = bno.get_system_status()
print('System status: {0}'.format(status))
print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
# Print out an error if system status is in error mode.
if status == 0x01:
    print('System error: {0}'.format(error))
    print('See datasheet section 4.3.59 for the meaning.')

# Print BNO055 software revision and other diagnostic data.
sw, bl, accel, mag, gyro = bno.get_revision()
print('Software version:   {0}'.format(sw))
print('Bootloader version: {0}'.format(bl))
print('Accelerometer ID:   0x{0:02X}'.format(accel))
print('Magnetometer ID:    0x{0:02X}'.format(mag))
print('Gyroscope ID:       0x{0:02X}\n'.format(gyro))

print('Reading BNO055 data, press Ctrl-C to quit...')

while True:

#    print("Temperature: {} degrees C".format(sensor.temperature))
#    print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
#    print("Magnetometer (microteslas): {}".format(sensor.magnetic))
#    print("Gyroscope (rad/sec): {}".format(sensor.gyro))
#    print("Euler angle: {}".format(sensor.euler))
#    print("Quaternion: {}".format(sensor.quaternion))
#    print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))


	try:
		

		while True:




			time.sleep(3)



			
			
			for i in range(512):
				for halfstep in range(8):
					for pin in range(4):
						x,y,orientation = bno.read_gravity()
						
						if (orientation != None):
						
							ControlPin[pin].value = seq[halfstep][pin]
							
							if orientation > 9.6 and orientation < 10:

								print(orientation)
								print("The camera is upright")
								print()
								print("Starting APRS")
								subprocess.call('python listTest.py', shell=True)

						time.sleep(0.00001)
					
	except TypeError:
		print("TypeError, Checking again")


	
