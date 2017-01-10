# Main File for Project
# Team 8.1
# Created 10/01/17
from microbit import *
import math
import radio

radio.on()
radio.config(channel == 85)

while True:
    
    display.show(Image.HEART)
    
    vals = accelerometer.get_values()
    
    data = str(math.sqrt(vals[0]**2+vals[1]**2+vals[2]**2))
    
    radio.send(data)
    
    sleep(100)
    
    

