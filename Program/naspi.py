import wiringpi2 as wpi
import time
import os


wpi.wiringPiSetup()


# bit 2, 1, 0
switchPin = [5, 6, 27]

#led yellow, green, blue
ledPin = [21, 26, 23]

def onYellow():
    wpi.digitalWrite(ledPin[0] ,1)

def offYellow():
    wpi.digitalWrite(ledPin[0] ,0)

def onGreen():
    wpi.digitalWrite(ledPin[1] ,1)

def offGreen():
    wpi.digitalWrite(ledPin[1] ,0)

def onBlue():
    wpi.digitalWrite(ledPin[2] ,1)

def offBlue():
    wpi.digitalWrite(ledPin[2] ,0)

def onStart():
    for pin in switchPin:
        wpi.pinMode(pin, 1)
    for pin in ledPin:
        wpi.pinMode(pin, 1)
    for blink in range(5):
        onYellow()
        time.sleep(0.25)
        offYellow()
        onGreen()
        time.sleep(0.25)
        offGreen()
        onBlue()
        time.sleep(0.25)
        offBlue()
        onGreen()
        time.sleep(0.25)
        offGreen()
    onYellow()

def resetSwitch():
    for pin in switchPin:
        wpi.digitalWrite(pin, 1)

def resetLeds():
    for pin in ledPin:
        wpi.digitalWrite(pin, 0)

def allLeds():
    for pin in ledPin:
        wpi.digitalWrite(pin, 1)

def ledsBlink():
    for times in range(20):
        for bitPos in range(3):
            wpi.digitalWrite(ledPin[bitPos], 1-wpi.digitalRead(switchPin[bitPos]))
        time.sleep(0.25)
        resetLeds()
        resetSwitch()
        time.sleep(0.25)

def getSwitch():
    resetSwitch()
    binary = str(1-wpi.digitalRead(switchPin[0])) +\
             str(1-wpi.digitalRead(switchPin[1])) +\
             str(1-wpi.digitalRead(switchPin[2]))
    switch = int(binary, 2)
#    print switch
    return float(switch)

def startSomething():
    onYellow()
    onGreen()

def endSomething():
    offGreen()
    onBlue()
    time.sleep(10)
    offBlue()

def main():
    onStart()
    while True:
        time.sleep(1)
        #print type(GPIO.input(inPin3))
        switch = getSwitch()
        if switch != 0:
            allLeds()
            time.sleep(1)
            resetLeds()
#            print('option selected: ' + str(switch))
            ledsBlink()
            switch = getSwitch()
            time.sleep(1)
            if switch == 0:
                print('undo option')
                onYellow()
                continue
            elif switch == 1:
                if getSwitch() == switch:
                    print('option 1')
                    startSomething()
                    os.system('mount /dev/sdc1 /mnt/USBDRIVE/')
                    os.system('cp -R /mnt/USBDRIVE/ /mnt/BACKUP1/_fromusb/')
                    os.system('umount /mnt/USBDRIVE/')
                    endSomething()
                onYellow()
            elif switch == 2:
                if getSwitch() == switch:
                    print('option 2')
                    print('Time backup the backup')
                    startSomething()
                    os.system('rsync -arv --delete /mnt/BACKUP1/ /mnt/BACKUP2/')
                    endSomething()
                onYellow()
            elif switch == 3:
                if getSwitch() == switch:
                    print('option 3')
                    startSomething()
                    os.system('git -C /home/odroid/Documents/NASPi/ pull')
                    endSomething()
                onYellow()
            elif switch == 4:
                if getSwitch() == switch:
                    print('option 4')
                    startSomething()
                    os.system('df -h > /mnt/BACKUP1/_diskspace.txt')
                    endSomething()
                onYellow()
            elif switch == 5:
                if getSwitch() == switch:
                    print('option 5')
                    print ('updateeeeeeeeeeee')
                    startSomething()
                    os.system('sudo apt-get -y update')
                    os.system('sudo apt-get -y upgrade')
                    os.system('sudo apt-get -y dist-upgrade')
                    endSomething()
                onYellow()
            elif switch == 6:
                if getSwitch() == switch:
                    print('option 6')
                    print('Time to reborn now')
                    startSomething()
                    os.system('shutdown now -h -r')
                onYellow()
            elif switch == 7:
                if getSwitch() == switch:
                    print('option 7')
                    print('Time to sleep now')
                    startSomething()
                    os.system("shutdown now -h")
                onYellow()
            else:
                print('unknown option')
                onYellow()
                continue

try:
    main()

except KeyboardInterrupt:
    for pin in ledPin:
        wpi.digitalWrite(pin, 0)
