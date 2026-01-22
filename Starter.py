from microbit import *
import radio

#This microbit if for sending START to runners and reset their state

GROUP = 188
radio.on()
radio.config(group=GROUP, power=7)

display.scroll("PRESS A TO START")

while True:
    if button_a.was_pressed():
        radio.send("START")
    
    if button_b.was_pressed():
        radio.send("RESET")
    

