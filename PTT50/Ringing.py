#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import os
from pin import Pin
from timeout import Timeout

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(Pin.Ringing, GPIO.OUT)
GPIO.output(Pin.Ringing, 1)

f = open("/home/pi/TwinklePTT50/ring.txt", "w")
f.write("0")
f.close()

x = 0
y = True
ring = 10#in ms
pause = 30#in ms

while(True):
    f = open("/home/pi/TwinklePTT50/ring.txt", "r")
    y = (f.readline(1) == "1")
    f.close()
    time.sleep(Timeout.Short)
    GPIO.output(Pin.Ringing, 1)

    while(y):
        f = open("/home/pi/TwinklePTT50/ring.txt", "r")
        y = (f.readline(1) == "1")
        f.close()
        time.sleep(Timeout.Short)
        x += 1
        #print(x)
        if(x % (ring + pause) == ring):
            #print('x')
            GPIO.output(Pin.Ringing, 0)
            print('Ring')
        if(x % (ring + pause) == (pause - ring)):
           #print('y')
           GPIO.output(Pin.Ringing, 1)
           print('No Ring')
GPIO.output(Pin.Ringing, 1)
