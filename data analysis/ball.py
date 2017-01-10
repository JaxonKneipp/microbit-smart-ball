from microbit import *
import math
import radio

radio.on()
radio.config(channel = 85)

while True:
    
    display.show(Image.HEART)
    vals = accelerometer.get_values()
    data = "{}, {}, {}, {}".format(running_time(), vals[0], vals[1], vals[2])
    radio.send(data)
    sleep(50)