from microbit import *
import radio

#Send end radio to runners
radio.on()
radio.config(group=10, power=7)

display.show(Image.HEART_SMALL)
while True:
    #End runner 1
    if button_a.was_pressed():
        radio.send("END1")

    #End runner2
    if button_b.was_pressed():
        radio.send("END2")
    
    sleep(20)


    
    
    


