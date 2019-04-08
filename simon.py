mport RPi.GPIO as GPIO
import wiringpi
from time import sleep
import random

#init GPIOS 
redLight = 12
redButton =  26

blueLight = 16
blueButton = 19

yellowLight = 20
yellowButton = 13

greenLight = 21
greenButton = 6

#Tone
redTone = 527
blueTone = 887
yellowTone = 745
greenTone = 469

greenTone = 469


#speaker GPIO
speaker = 5
wiringpi.wiringPiSetupGpio()
wiringpi.softToneCreate(speaker)

 
#initializations
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(redLight,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(redButton,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(blueLight,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(blueButton,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(yellowLight,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(yellowButton,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(greenLight,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(greenButton,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(greenButton,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)



# functions 
def whichButton():
        while (True):
                if(GPIO.input(redButton) == GPIO.HIGH):
                        ledOn(redLight,redTone)
                        return redLight
                if(GPIO.input(blueButton) == GPIO.HIGH):
                        ledOn(blueLight,blueTone)
                        return blueLight
                if(GPIO.input(yellowButton) == GPIO.HIGH):
                        ledOn(yellowLight,yellowTone)
                        return yellowLight
                if(GPIO.input(greenButton) == GPIO.HIGH):
                        ledOn(greenLight,greenTone)
                        return greenLight

# turn lights with sound
def ledOn(color, tone):
        GPIO.output(color, GPIO.HIGH)
        wiringpi.softToneWrite(speaker, tone)
        GPIO.output(color, GPIO.HIGH)
        wiringpi.softToneWrite(speaker, tone)
        sleep(0.5)
        GPIO.output(color, GPIO.LOW)
        wiringpi.softToneWrite(speaker, 0 )
        sleep(0.1)



def loser():
        print ( "you are a loser!")



#lets start playing simon!!

leds = []
gameOn = True
counter = 0
while (gameOn):
        leds.append(random.randint(0,3))
        for i in range (len(leds)):
                if leds[i] == 0:
                        ledOn(redLight, redTone)                        
                        if leds[i] == 0:
                        ledOn(redLight, redTone)
                if leds[i] == 1:
                        ledOn(blueLight, blueTone)
                if leds[i] == 2:
                        ledOn(yellowLight, yellowTone)
                if leds[i] == 3:
                        ledOn(greenLight, greenTone)

        counter = 0
        keepPlay = True
        while(keepPlay):
                while counter < len(leds):
              keepPlay = False

                        if ((whichButton() == blueLight) and (leds[counter] == 1)):
                                counter += 1
                                keepPlay = False
 
                        if ((whichButton() == yellowLight) and (leds[counter] == 2)):
                                counter += 1
                                keepPlay = False

                        if ((whichButton() == greenLight) and (leds[counter] == 3)):
                                counter += 1
                                keepPlay = False

                        else:
                                loser()
                                gameOn = False
                                keepPlay = False

print ( " you are a loser!")











