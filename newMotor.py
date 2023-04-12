# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Use this example for digital pin control of an H-bridge driver
# like a DRV8833, TB6612 or L298N.

import time
import board
import digitalio
from adafruit_motor import stepper

#200 steps per revolution
DELAY = 0.01
STEPS = 40

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

while True:
    for step in range(STEPS):
    motor.onestep()
    time.sleep(DELAY)




# for step in range(STEPS):
#     motor.onestep(direction=stepper.BACKWARD)
#     time.sleep(DELAY)

# for step in range(STEPS):
#     motor.onestep(style=stepper.DOUBLE)
#     time.sleep(DELAY)

# for step in range(STEPS):
#     motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
#     time.sleep(DELAY)

# for step in range(STEPS):
#     motor.onestep(style=stepper.INTERLEAVE)
#     time.sleep(DELAY)

# for step in range(STEPS):
#     motor.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
#     time.sleep(DELAY)


motor.release()
