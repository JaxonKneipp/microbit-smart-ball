# Main File for Project
# Team 8.1
# Created 10/01/17

from microbit import *
import math

while True:
    vals = accelerometer.get_values()
    print(str(math.sqrt(vals[0]**2+vals[1]**2+vals[2}**2)))
    
    sleep(500)
    
    

