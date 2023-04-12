from fileModificationHandler import FileModified
import subprocess
import time
import board
import digitalio
#import RPi.GPIO as GPIO
from collections import defaultdict
import csv

#GPIO.setmode(GPIO.BCM)

switch = digitalio.DigitalInOut(board.D9)

switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

led1 = digitalio.DigitalInOut(board.D4)
led2 = digitalio.DigitalInOut(board.D17)
led3 = digitalio.DigitalInOut(board.D27)
led4 = digitalio.DigitalInOut(board.D22)

led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
led3.direction = digitalio.Direction.OUTPUT
led4.direction = digitalio.Direction.OUTPUT

num1 = digitalio.DigitalInOut(board.D5)
num2 = digitalio.DigitalInOut(board.D6)
num3 = digitalio.DigitalInOut(board.D13)
num4 = digitalio.DigitalInOut(board.D19)


num1.direction = digitalio.Direction.OUTPUT
num2.direction = digitalio.Direction.OUTPUT
num3.direction = digitalio.Direction.OUTPUT
num4.direction = digitalio.Direction.OUTPUT

def file_modified():
    print("File Modified!")
    listTest()
    '''
    with open(r"logs7.txt", 'r+') as fp:
    # read an store all lines into list
        lines = fp.readlines()
    # move file pointer to the beginning of a file
        fp.seek(0)
    # truncate the file
        fp.truncate()

    # start writing lines except the first line
    # lines[1:] from line 2 to last line
        fp.writelines(lines[:-1])
    '''
    return False

def listTest():
    #import subprocess

    #subprocess.call('rtl_fm -f 144.390M - | direwolf -r 24000 -D 1 - -L logs7.txt', shell=True)


    # traverse through log file and find commands
    # put all the commands in a list
    columns = defaultdict(list) # each value in each column is appended to a list

    commands = []

    i = 0

    with open('logs7.txt') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for (k,v) in row.items():
                columns[k].append(v)
    '''
        spamreader = csv.reader(columns['comment'], delimiter=' ', quotechar='|')
        for row in spamreader:
            while i < len(row):
                commands.append(row[i])
                i+=1
    '''
    string = columns['comment'][len(columns['comment'])-1]
    commands = string.split()
    print(commands)

    # bools for status of greyscale, filter, and rotation
    grey = False
    filter = False
    flip = False


    # function to take pic with the correct settings on/off
    def take_pic():

        #normal pic with no effects
        if not grey and not filter and not flip:
            subprocess.call('libcamera-still --datetime --rotation 180', shell=True)

        #pic with image filter
        elif not grey and filter and not flip:
            subprocess.call('libcamera-still --datetime --brightness .5 --rotation 180', shell=True)

        # pic with image greyscale
        elif grey and not filter and not flip:
            subprocess.call('libcamera-still --datetime --saturation 0.0 --rotation 180', shell=True)

        #flip the pic 180 degrees
        elif not grey and not filter and flip:
            subprocess.call('libcamera-still --datetime', shell=True)

        # pic with image greyscale and filter
        elif grey and filter and not flip:
            subprocess.call('libcamera-still --datetime --saturation 0.0 --brightness .5 --rotation 180', shell=True)

        #pic with image greyscale and 180 degree flip
        elif grey and not filter and flip:
            subprocess.call('libcamera-still --datetime --saturation 0.0', shell=True)

        #pic with filter and 180 degree flip
        elif not grey and filter and flip:
            subprocess.call('libcamera-still --datetime --brightness .5', shell=True)

        #pic with everything
        elif grey and filter and flip:
            subprocess.call('libcamera-still --datetime --saturation 0.0 --brightness .5', shell=True)


    # MAIN LOGIC
    # Check each command and run the associated task
    for command in commands:

        if command == 'A1':
            print("Found A1, Turning Camera 60 Degrees to the Right")
            motorRight()

        elif command == 'B2':
            print("Found B2, Turning Camera 60 Degrees to the Left")
            motorLeft()

        elif command == 'C3':
            print("Found C3, Taking Picture")
            take_pic()

        elif command == 'D4':
            print("Found D4, Changing Camera Mode From Color to Grayscale")
            grey = True

        elif command == 'E5':
            print("Found E5, Changing Camera Mode From Grayscale to Color")
            grey = False

        elif command == 'F6':
            print("Found F6, Rotating Image 180 Degrees Upside Down")
            flip = not flip

        elif command == 'G7':
            print("Found G7, Special Effects Filter")
            filter = True

        elif command == 'H8':
            print("Found H8, Remove All Filters")
            filter = False

def motorLeft():
    #import RPi.GPIO as GPIO
    


    #GPIO.setmode(GPIO.BCM)



    #ControlPin = [4,17,27,22]
    ControlPin = [num1, num2, num3, num4]




    seq = [ [True,False,False,False],
	[True,False,False,False],
	[True,False,False,False],
	[False,True,False,False],
	[False,True,False,False],
	[False,True,False,False],
	[False,False,True,False],
	[False,False,True,False] ]

    for i in range(220):
        for halfstep in range(8):
            for pin in range(4):
                ControlPin[pin].value = seq[halfstep][pin]
			#GPIO.output(ControlPin[pin], seq[halfstep][pin])
            time.sleep(0.001)



def motorRight():






    


    #ControlPin = [4,17,27,22]
    ControlPin = [num1, num2, num3, num4]



    seq = [ [False,False,False,True],
	[False,False,False,True],
	[False,False,False,True],
	[False,False,True,False],
	[False,False,True,False],
	[False,False,True,False],
	[False,True,False,False],
	[False,True,False,False] ]
	
	
    for i in range(220):
        for halfstep in range(8):
            for pin in range(4):
                ControlPin[pin].value = seq[halfstep][pin]
			#GPIO.output(ControlPin[pin], seq[halfstep][pin])
            time.sleep(0.001)


    
def landing():
    print("Waiting for landing")

    while True:
        if (not switch.value):
            print()
            print("Starting Payload")
            print(not switch.value)
            print("Turning on APRS")
            break


def orientation():
    import sys
    print("Starting orientation")
    







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



    from Adafruit_BNO055 import BNO055



    bno = BNO055.BNO055(serial_port='/dev/serial0', rst=18)



    if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
        logging.basicConfig(level=logging.DEBUG)

    if not bno.begin():
        raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

    status, self_test, error = bno.get_system_status()
    print('System status: {0}'.format(status))
    print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
    
    if status == 0x01:
        print('System error: {0}'.format(error))
        print('See datasheet section 4.3.59 for the meaning.')


    sw, bl, accel, mag, gyro = bno.get_revision()
    print('Software version:   {0}'.format(sw))
    print('Bootloader version: {0}'.format(bl))
    print('Accelerometer ID:   0x{0:02X}'.format(accel))
    print('Magnetometer ID:    0x{0:02X}'.format(mag))
    print('Gyroscope ID:       0x{0:02X}\n'.format(gyro))

    print('Reading BNO055 data, press Ctrl-C to quit...')

    while True:

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
                                    return
								    #subprocess.call('python listTest.py', shell=True)

                            time.sleep(0.00001)
        except TypeError:
            print("TypeError, Checking again")


	


landing()
orientation()

subprocess.call('nohup rtl_fm -f 144.390M - | direwolf -r 24000 -D 1 - -L logs7.txt &', shell=True)


fileModifiedHandler = FileModified(r"logs7.txt",file_modified)
fileModifiedHandler.start()



