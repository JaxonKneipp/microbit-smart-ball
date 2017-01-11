# Receiver File for Project
# Team 8.1 (Balls)
# Created 10/01/17

from microbit import *
import radio 

radio.on()
radio.config(channel=85)

counter = 0

while True:
    
    msg = radio.receive()
    
    if str(msg) == "1":
        print('1')