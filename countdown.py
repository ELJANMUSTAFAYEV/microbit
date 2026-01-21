from microbit import *
import radio
import music
import time

def StartCountdown():
    music.play(['c5:1'])
    display.show("3")
    time.sleep(1)
        
    music.play(['c5:1'])
    display.show("2")
    time.sleep(1)
        
    music.play(['c5:1'])
    display.show("1")
    time.sleep(1)
        
    music.play(['e5:3'])
    display.show("GO")


while True:
    incoming = radio.receive()
    if incoming == 'StartCountdown':
        StartCountdown()
        radio.send('RunnersStart')
        
        
