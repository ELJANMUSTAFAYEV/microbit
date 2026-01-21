from microbit import *
start_time = 0
while True:
    incoming = radio.receive()
    if incoming == 'Start':
        start_time = running_time()
    if incoming == 'End1':
        elapsed_ms = running_time() - start_time
        Final_time1=(elapsed_ms // 1000)


