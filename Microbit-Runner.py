from microbit import *
import radio
import music

#This microbit is for runners, it has functions below
#1. Countdown 2. Count running time 3. Send time&total avgspeed to server 4. Reset state
runnerID = 1
distance = 50
endMessage = "END{}".format(runnerID)

radio.on()
radio.config(group=10, power=7)

#State
state = "idle" #idle - countdown - running - finished - settle
start_ms = None #avoid receiving multiple radios
reactionTime = None

def beep(ms=200):
    music.pitch(1000, ms)

def reset():
    global state, start_ms, reactionTime
    state = "idle"
    start_ms = None
    reactionTime = None
    display.clear()

def getAcceleration():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    acc = int((x*x + y*y + z*z) ** 0.5)
    return acc

def countdown_and_start():
    global state, start_ms, reactionTime
    state = "countdown"
    for i in range(3, 0, -1):
        display.show(str(i))
        beep(60)
        t1 = running_time()
        while running_time() - t1 <= 1000:
            if getAcceleration() >= 2000: #Anti false start system
                display.show("X")
                beep(1000)
                reset()
                return
            sleep(20)
    
    display.show("G")
    start_ms = running_time()
    state = "running"
    #Achieve the effect of multithreaded concurrency
    while running_time() - start_ms <= 5000:
        currTime = running_time() - start_ms
        if (0 <= currTime < 200) or (300 <= currTime < 500):
            beep(20)
        else:
            sleep(20)
        if getAcceleration() >= 2500 and reactionTime is None:
            reactionTime = (running_time() - start_ms) / 1000.0
        if currTime >= 500 and reactionTime is not None:
            sleep(300)
            display.clear()
            return reactionTime

reset()
display.show(str(runnerID))
while True:
    message = radio.receive()
    #Start
    if message == "START" and state == "idle":
        reactionTime = countdown_and_start()

    #End
    elif message == endMessage and state == "running":
        end_ms = running_time()
        totalSeconds = (end_ms - start_ms) / 1000.0
        
        if totalSeconds > 0:
            avgSpeed = distance / totalSeconds
        else:
            avgSpeed = float('inf')
        
        display.show("F")
        beep(100)
        sleep(300)
        display.clear()
        
        if reactionTime is not None:
            radio.send("Time:{}:{:.2f}".format(runnerID, totalSeconds))
            sleep(50)
            radio.send("Speed:{}:{:.2f}".format(runnerID, avgSpeed))
            sleep(50)
            radio.send("ReactionTime:{}:{:.2f}".format(runnerID, reactionTime))
        else:
            radio.send("Time:{}:NA".format(runnerID))
            sleep(50)
            radio.send("Speed:{}:NA".format(runnerID))
            sleep(50)
            radio.send("ReactionTime:{}:NA".format(runnerID))
        state = "finished"
        
    elif message == "RESET":
        reset()
        
    elif message and message.startswith("WIN") and state == "finished":
        parts = message.split(":")
        if len(parts) == 2 and int(parts[1]) in (1, 2):
            state = "settle"
            winner = int(parts[1])
            if winner == runnerID:
                display.show("W")
                beep(300)
                sleep(100)
                beep(300)
            else:
                display.show("L")
        
    sleep(20)



