"""Relay Example Code"""

# Import the libraries
# Digitalio is used to set up a pin as a digital input/output pin
import time
import board
import digitalio

# Set up Pin A1 as a digital in/out pin named relay
relay = digitalio.DigitalInOut(board.A1)
# Set the pin as an output pin
relay.direction = digitalio.Direction.OUTPUT

while True:

# This sets the signal on the relay pin to high, or 3.3V
    relay.value = True
    time.sleep(2)
# "False" sets the signal to low, or ~0V
    relay.value = False
    time.sleep(2)

# To change the time the LEDs are on or off, try changing the number in lines 18 or 21
# Keep it up - you're doing great!