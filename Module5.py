"""Surprise Code"""

import time
import board
from adafruit_apds9960.apds9960 import APDS9960
import pwmio
from adafruit_motor import servo
import digitalio

# Relay setup
relay = digitalio.DigitalInOut(board.A1)
relay.direction = digitalio.Direction.OUTPUT

# Servo setup
pwm = pwmio.PWMOut(board.A5, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

# Color sensor setup
i2c = board.I2C()
sensor = APDS9960(i2c)
sensor.enable_color = True

# Set up a counter for the while loop
cntr = 0

# This while loop will continue to run until the color red has been detected 3 times
while cntr < 3:
    for angle in range(0, 180, 10):
        my_servo.angle = angle
        color_rgb = sensor.color_data[:3]
        print(color_rgb)
# If the value of red exceeds 50, increment the counter
        red_threshold = 1.4*sum(color_rgb)/len(color_rgb)
        if color_rgb[0] > red_threshold:
            cntr = cntr + 1
# If the counter has reached 3, break out of the "while" loop
            if cntr > 3:
                break
        time.sleep(0.2)
# If red has not been detected 3 times yet, send the servo the other way
    for angle in range(180, 0, -10):
        my_servo.angle = angle
        color_rgb = sensor.color_data[:3]
        print(color_rgb)
# If the value of red exceeds 50, increment the counter
        red_threshold = 1.4*sum(color_rgb)/len(color_rgb)
        if color_rgb[0] > red_threshold:
            cntr = cntr + 1
# If the counter has reached 3, break out of the "while" loop
            if cntr > 3:
                break
        time.sleep(0.2)

# Now that the counter has reached 3, turn on the relay
relay.value = True

print("Congrats! You've completed the demo - now you can \
start designing your own experiment :)")
time.sleep(40)