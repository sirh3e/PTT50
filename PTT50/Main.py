
#!/usr/bin/python3

#Main Twinkle Script
#Active after Init
import RPi.GPIO as GPIO
import time
import os



GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40, GPIO.IN)#Takt
GPIO.setup(38, GPIO.IN)#Wählt
GPIO.setup(36, GPIO.IN)#Gabel

#Globale Variablen
x = 0
y = ""
z = 0

#functions
def main():
    while(True):
        listening()
        
def listening():
    if(GPIO.input(36) == 0):
        time.sleep(0.01)
        if(GPIO.input(36) == 1):
            os.system('twinkle --cmd answer')
    if(GPIO.input(36) == 1):
        if(GPIO.input(38) == 1):
            call()
        time.sleep(0.01)
        if(GPIO.input(36) == 0):
           os.system('twinkle --cmd bye')
                

def call():
    x = 0
    y = ""
    z = 0
    while(True):
        while(GPIO.input(38) == 1):
            z = 0
            if(GPIO.input(40) == 1):
                time.sleep(0.02)
                if(GPIO.input(40) == 0):
                    time.sleep(0.02)
                    x += 1
            if(GPIO.input(38) == 0 and x != 0):
                x %= 10
                #print(x)
                y += str(x)
                #print(y)
                x = 0
        time.sleep(0.02)
        z += 1
        if((z >= 300 and len(y) >= 3) or len(y) > 9):
           os.system('twinkle --call ' + y)
           x = 0
           y = ""
           z = 0
           main()
           #time.sleep(100)
        if(GPIO.input(36) == 0):
            x = 0
            y = ""
            z = 0
            #print('call abordet')
            main()
            #time.sleep(100)

#endOfFunctions
main()
#listening

    

