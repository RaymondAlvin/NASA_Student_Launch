import board
import digitalio
import time
import subprocess

switch = digitalio.DigitalInOut(board.D9)

switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.DOWN

#time.sleep(10)
print("Waiting for landing")

while True:
        if (switch.value):
                print()
                print("Starting Payload")
                print(switch.value)
                print("Orienting Camera..... (orientation4.py")
                subprocess.call('python orientation4.py', shell=True)
#               exit()

