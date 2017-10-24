import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

inPin1 = 17
inPin2 = 18
inPin3 = 27

outPin = 3

GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(inPin1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(inPin2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(inPin3, GPIO.IN, GPIO.PUD_DOWN)

##for i in range(0, 100):
##    GPIO.output(outPin, 1)
##    time.sleep(0.01)
##    GPIO.output(outPin, 0)
##    time.sleep(0.01)
##
##GPIO.output(outPin, 0)

##while True:
##    value = GPIO.input(inPin)
##    print value
##    if value == 0:
##        GPIO.output(outPin, 1)
###        time.sleep(0.1)
##    else:
##        GPIO.output(outPin, 0)
###        time.sleep(0.1)
##

##while True:
##    GPIO.output(outPin, 1)
##    valuetmp1 = GPIO.input(inPin)
##    print valuetmp1
##    time.sleep(1)
##    valuetmp2 = GPIO.input(inPin)
##    print valuetmp2
##    if valuetmp1 =! valuetmp2:
##        continue
##
##    if value == 0:
##        GPIO.output(outPin, 0)
##        time.sleep(5)
##        value2 = GPIO.input(inPin)
##        if value2 == 0:
##            print "Time to sleep now"
###            os.system("shutdown now -h")
##            continue
##        else:
##            print "pls"
##            GPIO.output(outPin, 1)
##            continue
###        time.sleep(0.1)


    

def fblink(switch):
    for sec in range(5):
##        print sec
        for blink in range(int(switch)):
##            print "blink" + str(blink)
            GPIO.output(outPin, 1)
            time.sleep(float(1/switch))
            GPIO.output(outPin, 0)
            time.sleep(float(1/switch))
        time.sleep(1)

def getswitch():
    binary = str(GPIO.input(inPin3)) + str(GPIO.input(inPin2)) + str(GPIO.input(inPin1))
    switch = int(binary, 2)
    return float(switch)

while True:
    GPIO.output(outPin, 1)
    time.sleep(1)
    #print type(GPIO.input(inPin3))
    switch = getswitch()
#    print int(binary, 2)

    if switch == 1:
        GPIO.output(outPin, 0)
        time.sleep(5)
        switch = getswitch()
        if switch == 1:
            fblink(switch)
            print "option 1"
            #confirmar?
        elif switch == 2:
            fblink(switch)
            print "option 2"
        elif switch == 3:
            fblink(switch)
            print "option 3"
        elif switch == 4:
            fblink(switch)
            print "option 4"
        elif switch == 5:
            fblink(switch)
            print "option 4"
        elif switch == 6:
            fblink(switch)
            print "option 6"
        elif switch == 7:
            fblink(switch)
            print "option 7"
        else:
            print "goback home"
            



        
##    valuetmp2 = GPIO.input(inPin)
##    print valuetmp2
##    if valuetmp1 =! valuetmp2:
##        continue
##
##    if value == 0:
##        GPIO.output(outPin, 0)
##        time.sleep(5)
##        value2 = GPIO.input(inPin)
##        if value2 == 0:
##            print "Time to sleep now"
###            os.system("shutdown now -h")
##            continue
##        else:
##            print "pls"
##            GPIO.output(outPin, 1)
##            continue
###        time.sleep(0.1)
##   


GPIO.cleanup()
