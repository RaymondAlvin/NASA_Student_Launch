import time
import board
import adafruit_bno055
import RPi.GPIO as GPIO
import digitalio
import logging
import sys
from Adafruit_BNO055 import BNO055
from adafruit_motor import stepper

#motor configuration
#200 steps per revolution
DELAY = 0.01
STEPS = 20

# You can use any available GPIO pin on both a microcontroller and a Raspberry Pi.
# The following pins are simply a suggestion. If you use different pins, update
# the following code to use your chosen pins.

coils = (
    digitalio.DigitalInOut(board.D19),  # A1
    digitalio.DigitalInOut(board.D26),  # A2
    digitalio.DigitalInOut(board.D20),  # B1
    digitalio.DigitalInOut(board.D21),  # B2
)

for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT
    
motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)



#imu configuration
last_val = 0xFFFF

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
print()











#    print("Temperature: {} degrees C".format(sensor.temperature))
#    print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
#    print("Magnetometer (microteslas): {}".format(sensor.magnetic))
#    print("Gyroscope (rad/sec): {}".format(sensor.gyro))
#    print("Euler angle: {}".format(sensor.euler))
#    print("Quaternion: {}".format(sensor.quaternion))
#    print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))

while True:
  
  try:
		

		while True:




			time.sleep(3)
      for step in range(STEPS):
        motor.onestep()
        time.sleep(DELAY)
        
        x,y,orientation = bno.read_gravity()
        if orientation > 9.6 and orientation < 10:

								print(orientation)
								print("The camera is upright")
								print()
								print("Starting APRS")
								return
					
	except TypeError:
		print("TypeError, Checking again")

    
motor.release()

	
