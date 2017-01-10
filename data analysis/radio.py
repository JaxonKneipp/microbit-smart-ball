from microbit import *
import radio 

radio.on()
radio.config(channel=85)

while True:
    message = radio.receive()    
    
    if message:
        print(message)