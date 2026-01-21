from microbit import *

DISTANCE = 50  # meters

# real_val comes from the stopwatch
# time_sec = real_value   
time_sec = 7.9

if time_sec > 0:
    speed_mps2 = DISTANCE / time_sec        # meters per second
    speed_kmh2 = speed_mps2 * 3.6             # convert to km/h

    display.scroll(str(round(speed_kmh2, 1)) + " kmh")
else:
    display.scroll("ERR")
