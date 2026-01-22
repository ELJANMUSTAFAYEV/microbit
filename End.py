from microbit import *
import radio

#Send end radio to runners

GROUP = 188

radio.on()
radio.config(group=GROUP, power=7)

display.scroll("A to 1, B to 2")

while True:
    #End runner 1
    if button_a.was_pressed():
        radio.send("END1")
        display.show("1")
        sleep(200)
        display.clear()

    #End runner2
    if button_b.was_pressed():
        radio.send("END2")
        display.show("2")
        sleep(200)
        display.clear()


    
    
    
