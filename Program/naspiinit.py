import RPi.GPIO as GPIO
import time
import os



GPIO.setmode(GPIO.BCM)

inPin1 = 11
inPin2 = 9
inPin3 = 10

outPin = 22

GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(inPin1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(inPin2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(inPin3, GPIO.IN, GPIO.PUD_DOWN)

  

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
    binary = str(GPIO.input(inPin1)) + str(GPIO.input(inPin2)) + str(GPIO.input(inPin3))
    switch = int(binary, 2)
#    print switch
    return float(switch)

def main():
    GPIO.output(outPin, 1)
    time.sleep(10)
    GPIO.output(outPin, 0)
    while True:
        
        time.sleep(1)
        #print type(GPIO.input(inPin3))
        switch = getswitch()
    	if switch != 0:
            GPIO.output(outPin, 1)
            time.sleep(5)
            GPIO.output(outPin, 0)
            print 'option selected: ' + str(switch)

        switch = getswitch()
        if switch == 1:
            fblink(switch)
            if getswitch() == switch:
                print "option 1"
                print "Time to sleep now"
                os.system("shutdown now -h")
        elif switch == 2:
            fblink(switch)
            if getswitch() == switch:
                print "option 2"
                print "Time to reborn now"
                os.system("shutdown now -h -r")
        elif switch == 3:
            fblink(switch)
            if getswitch() == switch:
                print "option 3"
        elif switch == 4:
            fblink(switch)
            if getswitch() == switch:
                print "option 4"
        elif switch == 5:
            fblink(switch)
            if getswitch() == switch:
                print "option 5"
        elif switch == 6:
            fblink(switch)
            if getswitch() == switch:
                print "option 6"
        elif switch == 7:
            fblink(switch)
            if getswitch() == switch:
                print "option 7"
        else:
#            print 'undo option'
            continue
        
    GPIO.cleanup()

try:
    main()

except KeyboardInterrupt:
    GPIO.cleanup()
