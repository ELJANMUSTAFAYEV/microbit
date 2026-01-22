from microbit import *
import radio

#This microbit is for runners, it has functions below
#1. Countdown 2. Count running time 3. Send time&total avgspeed to server 4. Reset state

GROUP = 188
runnerID = 1
distance = 50
endMessage = "END{}".format(runnerID)

radio.on()
radio.config(group=GROUP, power=7)


#State
state = "idle" #idle - countdown - running - finished 
start_ms = None #avoid receiving multiple radios

def beep(ms):
    pin0.write_digital(1)
    sleep(ms)
    pin0.write_digital(0)

def reset():
    global state, start_ms
    state = "idle"
    start_ms = None
    display.clear()

def countdown_and_start():
    global state, start_ms
    state = "countdown"
    for i in range(3, 0, -1):
        display.show(str(i))
        beep(60)  
        sleep(1000)
    display.show("G")
    beep(200)
    sleep(100)
    beep(200) 
    start_ms = running_time()
    state = "running"
    sleep(300)
    display.clear()

reset()

while True:
    message = radio.receive()

    #Start
    if message == "START" and state == "idle":
        countdown_and_start()

    #End
    elif message == endMessage and state == "running":
        end_ms = running_time()
        totalSeconds = (end_ms - start_ms) / 1000.0
        
        if totalSeconds > 0:
            avgSpeed = distance / totalSeconds
        else:
            avgSpeed = float('inf')

        display.scroll("Time: {:.2f}s".format(totalSeconds))
        display.scroll("Speed: {:.2f}".format(avgSpeed))
        radio.send("Time:{}:{:.2f}".format(runnerID, totalSeconds))
        radio.send("Speed:{}:{:.2f}".format(runnerID, avgSpeed))

        state = "finished"
        
    elif message == "RESET":
        reset()
