# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_bno055
import RPi.GPIO as GPIO
import digitalio



i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)


led1 = digitalio.DigitalInOut(board.D4)
led2 = digitalio.DigitalInOut(board.D17)
led3 = digitalio.DigitalInOut(board.D27)
led4 = digitalio.DigitalInOut(board.D22)

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


def temperature():
	global last_val  
	result = sensor.temperature
	if abs(result - last_val) == 128:
		result = sensor.temperature
		if abs(result - last_val) == 128:
			return 0b00111111 & result
	last_val = result
	return result


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
						orientation = sensor.gravity[2]
						
						if (orientation != None):
						
							ControlPin[pin].value = seq[halfstep][pin]
							
							if orientation > 9.6 and orientation < 10:

								print(orientation)
								print("The camera is upright")
								print()
								print("Starting APRS")
								subprocess.call('python listTest.py', shell=True)

						time.sleep(0.001)
					
	except TypeError:
		print("TypeError, Checking again")


	
