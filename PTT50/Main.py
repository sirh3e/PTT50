#!/usr/bin/python3

#Main Twinkle Script
#Active after Init
import RPi.GPIO as GPIO
import time
import os
from enum import Enum
from pin import Pin
from timeout import Timeout

#Globale Variablen
x = 0
y = ""
z = 0

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(Pin.Pulse, GPIO.IN)
    GPIO.setup(Pin.Calling, GPIO.IN)
    GPIO.setup(Pin.Fork, GPIO.IN)

#functions
def main():
    while(True):
        listening()

def listening():
    if(GPIO.input(Pin.Fork)):
        if(GPIO.input(Pin.Calling)):
            call()
        time.sleep(Timeout.Short)
        if(GPIO.input(Pin.Fork) == 0):
           os.system('twinkle --cmd bye')
    else:
        time.sleep(Timeout.Short)
        if(GPIO.input(Pin.Fork)):
            os.system('twinkle --cmd answer')

def call():
    x = 0
    y = ""
    z = 0
    while(True):
        while(GPIO.input(Pin.Calling)):
            z = 0
            if(GPIO.input(Pin.Pulse)):
                time.sleep(Timeout.Long)
                if(GPIO.input(Pin.Pulse) == 0):
                    time.sleep(Timeout.NotAny)
                    x += 1
            if(GPIO.input(Pin.Calling) == 0 and x != 0):
                x %= 10
                #print(x)
                y += str(x)
                #print(y)
                x = 0
        time.sleep(Timeout.Long)
        z += 1
        if((z >= 300 and len(y) >= 3) or len(y) > 9):
           os.system('twinkle --call ' + y)
           x = 0
           y = ""
           z = 0
           main()
           #time.sleep(100)
        if(GPIO.input(Pin.Fork) == 0):
            x = 0
            y = ""
            z = 0
            #print('call abordet')
            main()
            #time.sleep(100)

if __name__ == '__main__':
    #endOfFunctions
    setup()
    main()
    #listening
