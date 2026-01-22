from microbit import *
import radio

#Transferring data to the PC

GROUP = 188

radio.on()
radio.config(group=GROUP, power=7)

display.scroll("Server")

while True:
    message = radio.receive()
    if message.startswith("Time:") or message.startswith("Speed:"):
        print(message)
        display.show(Image.SMILE)
        sleep(50)
        display.clear()


