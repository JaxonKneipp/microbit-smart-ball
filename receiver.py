# Receiver File for Project
# Team 8.1 (Balls)
# Created 10/01/17

from microbit import *

radio.on()
radio.config(channel=85)
while True:
    msg = radio.receive()
    if msg:
        print(msg)