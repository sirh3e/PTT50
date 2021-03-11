#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(32, GPIO.OUT)#Ringing
GPIO.output(32, 1)

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
    time.sleep(0.1)
    GPIO.output(32, 1)

    while(y):
        f = open("/home/pi/TwinklePTT50/ring.txt", "r")
        y = (f.readline(1) == "1")
        f.close()
        time.sleep(0.1)
        x += 1
        #print(x)
        if(x % (ring + pause) == ring):
            #print('x')
            GPIO.output(32, 0)
            print('Ring')
        if(x % (ring + pause) == (pause - ring)):
           #print('y')
           GPIO.output(32, 1)
           print('No Ring')
GPIO.output(32, 1)
