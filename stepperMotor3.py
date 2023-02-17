#import RPi.GPIO as GPIO
import time
import board
import digitalio
import RPi.GPIO as GPIO


#GPIO.setmode(GPIO.BCM)


led1 = digitalio.DigitalInOut(board.D5)
led2 = digitalio.DigitalInOut(board.D6)
led3 = digitalio.DigitalInOut(board.D13)
led4 = digitalio.DigitalInOut(board.D19)

led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
led3.direction = digitalio.Direction.OUTPUT
led4.direction = digitalio.Direction.OUTPUT


#ControlPin = [4,17,27,22]
ControlPin = [led1, led2, led3, led4]

'''
for pin in ControlPin:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)
'''


seq = [ [True,False,False,False],
	[True,False,False,False],
	[True,False,False,False],
	[False,True,False,False],
	[False,True,False,False],
	[False,True,False,False],
	[False,False,True,False],
	[False,False,True,False] ]

for i in range(512):
	for halfstep in range(8):
		for pin in range(4):
			ControlPin[pin].value = seq[halfstep][pin]
			#GPIO.output(ControlPin[pin], seq[halfstep][pin])
		time.sleep(0.001)


GPIO.cleanup()
