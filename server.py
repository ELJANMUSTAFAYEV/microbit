
import radio
from microbit import *
lt=list()
time=0
last=0
while True:
    

   message=radio.receive()
   try:
       lt.append((time,int(message)))
       last=int(message)
   except:
       lt.append((time,(last)))
   sleep(1000)
   time+=1
