subprocess.call('rtl_fm -f 144.390M - | direwolf -r 24000 -D 1 - -L logs7.txt', shell=True)


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

    spamreader = csv.reader(columns['comment'], delimiter=' ', quotechar='|')
    for row in spamreader:
        while i < len(row):
            commands.append(row[i])
            i+=1

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
		subprocess.call('python stepperMotor3.py', shell=True)

	elif command == 'B2':
		print("Found B2, Turning Camera 60 Degrees to the Left")
		subprocess.call('python stepperMotor3.py', shell=True)

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


