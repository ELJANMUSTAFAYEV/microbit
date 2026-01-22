
import radio
from microbit import *
lt=list()
time=0
last=0
radio.on()
while True:
    

   message=radio.receive()
   try:
       lt.append((time,int(message)))
       last=int(message)
   except:
       lt.append((time,(last)))
   sleep(1000)
   time+=1

import matplotlib.pyplot as plt
import random 
plt.ion()
fig=plt.figure()

ax=fig.add_subplot(111)
ax.set_ylabel("speed")
ax.set_xlabel("time")
ax.set_title("RACE")
ax.set_xticks([i for i in range(0,10,1)])
ax.set_yticks([i for i in range(0,100,5)])
ax.minorticks_off()


x=[ i for i in range(0,10,1)]
y=[random.randint(0,100) for _ in range(10) ]
line,=ax.plot([],[],marker='o',color='blue')
line2,=ax.plot([],[],marker='o',color='red')
y1=[random.randint(0,100) for _ in range(10) ]
total=100
step=0
while step<total:
    step=step+1
    line.set_data(x[:step],y[:step])
    line2.set_data(x[:step],y1[:step])

    plt.draw()
    plt.pause(.2)
    

