import radio
while True:
    if button_a.was_pressed():
        radio.send('End1') #Stop runner 1 timmer
    if button_b.was_pressed():
        radio.send('End2') #Stop runner 2 timmer
