from microbit import *
import radio          

radio.on()            
radio.config(group=23)  

DISTANCE = 50  # meters

# real_val comes from the stopwatch
# time_sec = real_value
time_sec = 7.9

if time_sec > 0:
    speed_mps2 = DISTANCE / time_sec   # meters per second

    radio.send(str(speed_mps2))        

else:
    display.scroll("ERR")

