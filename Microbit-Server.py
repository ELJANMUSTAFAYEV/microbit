from microbit import *
import radio

#Transferring data to the PC

GROUP = 10

radio.on()
radio.config(group=GROUP, power=7)

display.show("S")

winner = None

def sendWinner(winID):
    for i in range(5):
        radio.send("WIN:{}".format(winID))
        sleep(80)

while True:
    message = radio.receive()
    
    if not message:
        sleep(5)
        continue
    
    if message.startswith("Time:") or message.startswith("Speed:") or message.startswith("ReactionTime:"):
        print(message)
        display.clear()
        
    if message == "RESET":
        winner = None
        display.clear()
        
    if winner is None and message.startswith("Time:"):
        parts = message.split(":")
        if len(parts) == 3:
            try:
                winID = int(parts[1])
                if winID in (1, 2):
                    winner = winID
                    sendWinner(winner)
                    display.show("Y")
            except:
                pass
    
    sleep(5)


