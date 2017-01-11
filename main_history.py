# Main File for Project
# Team 8.1
# Created 10/01/17

from microbit import *
import math
import radio
import music

radio.on()
radio.config(channel = 85)

while True:
    watchingForCatch = False
    throw_deadline = False
    acc_history = [1000]
    differences = [0]
    catchtime_start = 0
    
    msg = radio.receive()
    display.show(Image.HAPPY)
    if msg == 'start':
        while True:
            display.show(Image.HEART)
            vals = accelerometer.get_values()
            data = math.sqrt(vals[0]**2+vals[1]**2+vals[2]**2)
            acc_history.append(data)
            
            if len(acc_history) > 15:
                acc_history.pop(0)
            
            diff = acc_history[-2] - acc_history[-1]
            differences.append(diff)

            if len(differences) > 15:
                differences.pop(0)
                
            if not watchingForCatch: #thrown
                if (max(differences) > 1000) and (min(differences) < -1000):
                    differences = [0]
                    radio.send("0")
                    catchtime_start = running_time()
                    watchingForCatch = True
                    throw_deadline = False
                
            if watchingForCatch: #caught
                if (max(differences) > 1000) and (min(differences) < -1000):
                    differences = [0]
                    catchtime_start = running_time()
                    throw_deadline = True
                    radio.send("1")
                    watchingForCatch = False
             
            if running_time() - catchtime_start >= 3000 and throw_deadline:
                radio.send("game over")
                display.show(Image.SKULL)
                music.play(music.DADADADUM)
                break
            
            sleep(50)
    sleep(50)