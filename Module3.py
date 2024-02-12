"""Color Sensor Example Code"""
# Will detect the color from the sensor and print it out every second.

# First import the necessary libraries
# In this example, adafruit_apds9960 is the color sensor library
import time
import board
from adafruit_apds9960.apds9960 import APDS9960

# Create sensor object, communicating over the board's default I2C bus
# This tells the M4 to use the SDA and SCL pins
i2c = board.I2C()
# Then, it sets up the color sensor as the device on those pins
sensor = APDS9960(i2c)
sensor.enable_color = True

# Main loop reading color and printing it every second.
# "While" loops run constantly as long as the condition is true
# In this case the condition is "True" which will never change, meaning
# "while True:" is used to create an infinite loop
while True:
    
    # The first step to reading the data is to pull it from the sensor
    # In this case, the RGB values are the first 3 values from the sensor
    color_rgb = sensor.color_data[:3]
    # Then, those values are printed to the serial monitor for you to read
    print("RGB color as 16 bits 3-tuple: {}".format(color_rgb))
    time.sleep(1)
    
# This code will run infinitely, so just unplug the M4 when you're done
# Have fun!