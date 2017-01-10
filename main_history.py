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
acc_history = []


while True:
    
    catchtime_start = 0
    display.show(Image.HEART)
    vals = accelerometer.get_values()
    data = math.sqrt(vals[0]**2+vals[1]**2+vals[2]**2)
    acc_history.append(data)
    diff = vals[-1] - vals[-2]
    
    if len(acc_history) > 15:
        acc_history.pop(0)
    
    
    
    print(acc_history)
    average = sum(acc_history)/ len(acc_history)
        
    if average <= 700 and not watchingForCatch: #thrown
        
        radio.send("0")
        watchingForCatch = True
        throw_deadline = False
        
    if watchingForCatch and average >= 3500: #caught
        
        catchtime_start = running_time()
        throw_deadline = True
        radio.send("1")
        watchingForCatch = False
     
    if running_time() - catchtime_start >= 5000 and throw_deadline:
        radio.send("game over")
        display.show(Image.SKULL)
        break
     
     
    sleep(50)
