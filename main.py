# Main File for Project
# Team 8.1
# Created 10/01/17
from microbit import *
import math
import radio

radio.on()
radio.config(channel = 85)

watchingForCatch = False
throw_deadline = False

while True:
    
    catchtime_start = 0
    display.show(Image.HEART)
    vals = accelerometer.get_values()
    data = math.sqrt(vals[0]**2+vals[1]**2+vals[2]**2)
    
    if data <= 650 and not watchingForCatch: #thrown
        
        radio.send("0")
        watchingForCatch = True
        throw_deadline = False
        
    if watchingForCatch and data >= 1500: #caught
        
        catchtime_start = running_time()
        throw_deadline = True
        radio.send("1")
        watchingForCatch = False
     
    if running_time() - catchtime_start >= 8000 and throw_deadline:
        radio.send("game over")
        display.show(Image.SKULL)
        break
     
    sleep(100)
    
    
    

