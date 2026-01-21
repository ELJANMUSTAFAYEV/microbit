from microbit import *

DISTANCE = 50  # meters

# real_val comes from the stopwatch
# time_sec = real_value1   
time_sec = 7.9

if time_sec > 0:
    speed_mps1 = DISTANCE / time_sec        # meters per second
    speed_kmh1 = speed_mps1 * 3.6             # convert to km/h

    display.scroll(str(round(speed_kmh, 1)) + " kmh")
else:
    display.scroll("ERR")