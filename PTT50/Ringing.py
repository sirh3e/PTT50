#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import os
from config import Config
from pin import Pin
from timeout import Timeout
from utilities import read_from_file_is_not_ringing, write_is_ringing

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(Pin.Ringing, GPIO.OUT)
    GPIO.output(Pin.Ringing, 1)

    prepare()

def prepare():
    write_is_ringing(Config.RING_FILE_PATH)

def main():
    x = 0
    y = True
    ring = 10#in ms
    pause = 30#in ms
    
    while(True):
        y = read_from_file_is_not_ringing(Config.RING_FILE_PATH)
        time.sleep(Timeout.Short)
        GPIO.output(Pin.Ringing, 1)

        while(y):
            y = read_from_file_is_not_ringing(Config.RING_FILE_PATH)
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
