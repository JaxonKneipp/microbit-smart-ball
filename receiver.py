# Receiver File for Project
# Team 8.1 (Balls)
# Created 10/01/17

from microbit import *
import radio
import music

radio.on()
radio.config(channel=85)

counter = 1

while True:
    msg = radio.receive()

    if str(msg) == "1":
        counter += 1
        print("count {}".format(counter))
        display.scroll(str(counter), wait= False)

    if str(msg) == "game over":
        print("over")
        display.show(Image.SKULL)
        music.play(music.WAWAWAWAA)
        display.show('Z')
        
    if button_a.was_pressed():
        radio.send("start" )
        counter = 1
        display.clear()
        music.play(music.BA_DING)