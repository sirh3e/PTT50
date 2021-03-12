#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import os
from pin import Pin
from timeout import Timeout
from utilities import write_is_ringing

path = "/home/pi/TwinklePTT50/ring.txt"

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(Pin.Ringing, GPIO.OUT)
    GPIO.output(Pin.Ringing, 1)

    prepare()

def prepare():
    write_is_ringing(path)

def is_ringing(path):
    #ToDo check if file exits
    with open(path, "r") as file:
       return file.readline(1) == "1"

def main():
    x = 0
    y = True
    ring = 10#in ms
    pause = 30#in ms
    
    while(True):
        y = is_ringing(path)
        time.sleep(Timeout.Short)
        GPIO.output(Pin.Ringing, 1)

        while(y):
            y = is_ringing(path)
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

if __name__ == '__main__':
    setup()
    main()
