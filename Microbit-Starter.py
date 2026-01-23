from microbit import *
import radio

#This microbit if for sending START to runners and reset their state
radio.on()
radio.config(group=10, power=7)

display.show(Image.HEART)
while True:
    if button_a.was_pressed():
        radio.send("START")
    
    if button_b.was_pressed():
        radio.send("RESET")
    
    sleep(20)
    



