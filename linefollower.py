import sys
import time
import RPi.GPIO as GPIO



#IO.setmode(IO.BCM)
mode=GPIO.getmode()
 
#TO ASSIGN PIN

LeftIR=11
RightIR=13
StepPinForward1=21
StepPinBackward1=19
StepPinForward2=23
StepPinBackward2=24
sleeptime=1
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)

#TO CONFIGURE PIN AS IN OR OUT PIN

GPIO.setup(LeftIR,GPIO.IN) #GPIO 2 -> Left IR out
GPIO.setup(RightIR,GPIO.IN) #GPIO 3 -> Right IR out
GPIO.setup(StepPinForward1,GPIO.OUT) #GPIO 4 -> Motor 1 terminal A
GPIO.setup(StepPinBackward1,GPIO.OUT) #GPIO 14 -> Motor 1 terminal B
GPIO.setup(StepPinForward2,GPIO.OUT) #GPIO 17 -> Motor Left terminal A
GPIO.setup(StepPinBackward2,GPIO.OUT) #GPIO 18 -> Motor Left terminal B

while 1:

    if(GPIO.input(LeftIR) == False and GPIO.input(RightIR) == False): #both while move forward     

        GPIO.output(StepPinForward1,True) #1A+

        GPIO.output(StepPinBackward1,False) #1B-

        GPIO.output(StepPinForward2,True) #2A+

        GPIO.output(StepPinBackward2,False)

    elif(GPIO.input(LeftIR) == False and GPIO.input(RightIR) == True): #turn right  

        GPIO.output(StepPinForward1,True) #1A+

        GPIO.output(StepPinBackward1,True) #1B-

        GPIO.output(StepPinForward2,True) #2A+

        GPIO.output(StepPinBackward2,False) #2B-

    elif(GPIO.input(LeftIR) == True and GPIO.input(RightIR) == False): #turn left

        GPIO.output(StepPinForward1,True) #1A+

        GPIO.output(StepPinBackward1,False) #1B-

        GPIO.output(StepPinForward2,True) #2A+

        GPIO.output(StepPinBackward2,True) #2B-

    else:  #stay still

        GPIO.output(StepPinForward1,True) #1A+

        GPIO.output(StepPinBackward1,True) #1B-

        GPIO.output(StepPinForward2,True) #2A+

        GPIO.output(StepPinBackward2,True) #2B-
        
GPIO.cleanup()
