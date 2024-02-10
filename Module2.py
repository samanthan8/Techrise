"""Servo Example Code"""


# The first part of any code is the imports, or libraries
# You can think of these as the toolboxes for the M4
# For example, the first one below is "import time"
# This tells the M4 that the code will be using a timer

import time
import board
import pwmio
from adafruit_motor import servo


# Create a PWMOut object on Pin A5
# This sets up the signals to be sent to the servo to control the angle
pwm = pwmio.PWMOut(board.A5, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
# Using the adafruit_motor library, "servo" sets up an easy code interface
# From here, all you need to do is input the angle
my_servo = servo.Servo(pwm)

# "For" loops are used to run the same section of code with incrementing values
# In this example, the servo angle starts at 0 and increments by 5 up to 180
for angle in range(0, 180, 5):
    my_servo.angle = angle
    time.sleep(0.05)
# After it reaches 180 degrees, it will step back down to 0
for angle in range(180, 0, -5):
    my_servo.angle = angle
    time.sleep(0.05)

# The code is finished running!