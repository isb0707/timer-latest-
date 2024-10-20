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
print("all of you are standing up right now")

sit_down_list = [] #create an empty list there is no player in it at the very beginning


im = Image.open("times-up.jpeg")

# Set the timer to sleep for a random time between 10 to 25 seconds
set_time = int(random.randint(10,25))

print('you have to sleep for ' +str(set_time))
start_time = time.time() #create a variable to record a point for 'start time'

while time.time() - start_time < set_time: #here time.time()is right now
    sit_down_name = input('enter the name for person who sat down: ')
    sit_down_list.append(sit_down_name)
    if time.time() - start_time >= set_time:
        print('Times up')
        break

winner = sit_down_list[-1]
print(f"The last person to sit down is: {winner}. you win!")
print("Players still standing are eliminated.")


im.show()

