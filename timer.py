"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
timer.py also uses the random library to return a random time period
"""


# This program is timer that counts down

import time # The time library has a sleep function that will pause the script for a specifized amount of time
import random # The random library allows the function to generate the random time for the program to sleep
from PIL import Image # the pillow library makes it easy to display images 
print("Players stand")
im = Image.open("times-up.jpeg")

# Set the timer to sleep for a random time between 10 to 25 seconds
set_time = int(random.randint(10,25))

time.sleep(set_time)

im.show()

