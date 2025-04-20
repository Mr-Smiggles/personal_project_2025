import RPi.GPIO as GPIO
import pygame
from time import sleep
running = True
pygame.init()
x = 70
y = 70
#setup controller

#initialize controller
for event in pygame.event.get():
    if event.type == pygame.JOYDEVICEADDED:
        print(event)
        controller = pygame.joystick.Joystick(event.device_index)
        controller.init()  # Initialize the joystick
    elif event.type == pygame.QUIT:
        running = False

def goFoward():
    GPIO.output(AN11,GPIO.LOW)
    GPIO.output(AN12,GPIO.HIGH)
    GPIO.output(BN11,GPIO.LOW)
    GPIO.output(BN12,GPIO.HIGH)
    GPIO.output(AN21,GPIO.LOW)
    GPIO.output(AN22,GPIO.HIGH)
    GPIO.output(BN21,GPIO.LOW)
    GPIO.output(BN22,GPIO.HIGH)

def goBackward():
    GPIO.output(AN11,GPIO.HIGH)
    GPIO.output(AN12,GPIO.LOW)
    GPIO.output(BN11,GPIO.HIGH)
    GPIO.output(BN12,GPIO.LOW)
    GPIO.output(AN21,GPIO.HIGH)
    GPIO.output(AN22,GPIO.LOW)
    GPIO.output(BN21,GPIO.HIGH)
    GPIO.output(BN22,GPIO.LOW)

def rotateRight():
    GPIO.output(AN11,GPIO.HIGH)
    GPIO.output(AN12,GPIO.LOW)
    GPIO.output(BN11,GPIO.HIGH)
    GPIO.output(BN12,GPIO.LOW)
    GPIO.output(AN21,GPIO.HIGH)
    GPIO.output(AN22,GPIO.LOW)
    GPIO.output(BN21,GPIO.HIGH)
    GPIO.output(BN22,GPIO.LOW)

def rotateLeft():
    GPIO.output(AN11,GPIO.LOW)
    GPIO.output(AN12,GPIO.HIGH)
    GPIO.output(BN11,GPIO.LOW)
    GPIO.output(BN12,GPIO.HIGH)
    GPIO.output(AN21,GPIO.LOW)
    GPIO.output(AN22,GPIO.HIGH)
    GPIO.output(BN21,GPIO.LOW)
    GPIO.output(BN22,GPIO.HIGH)

def main():
    if controller.get_init():  # Check if the controller is initialized
   
        #get left joystick raw x and y values and trigger values
        leftstickX = controller.get_axis(0) * 100  # gets left joystick x-axis
        leftstickY = controller.get_axis(1) * -100  # gets left joystick y-axis
        leftTrigger = controller.get_axis(2) * 100
        rightTrigger = controller.get_axis(5) * 100


        #applies controller deadzone
        if leftstickX >= 5 or leftstickX <= -5:
            lx = leftstickX
        else:
            lx = 0

        if leftstickY >= 5 or leftstickY <= -5:
            ly = leftstickY
        else:
            ly = 0
        
        if leftTrigger >= 5:
            lt = leftTrigger
        else:
            lt = leftTrigger - leftTrigger
        
        if rightTrigger >= 5:
            rt = rightTrigger
        else:
            rt = rightTrigger - rightTrigger

        print(ly, lt, rt, end='\r')


        if ly >= 0:
            goFoward()
            p1.ChangeDutyCycle(ly)#Set the P1 pulse signal duty cycle to the value of y joystick%
            p2.ChangeDutyCycle(ly)#Set the P2 pulse signal duty cycle to y joystick% 
        
        elif ly < 0:
            goBackward()
            p1.ChangeDutyCycle(-ly)#Set the P1 pulse signal duty cycle to the value of y joystick%
            p2.ChangeDutyCycle(-ly)#Set the P2 pulse signal duty cycle to y joystick% 

        
        if lt > 0:
            rotateLeft()
            p1.ChangeDutyCycle(lt)#Set the P1 pulse signal duty cycle to the value of y joystick%
            p2.ChangeDutyCycle(lt)#Set the P2 pulse signal duty cycle to y joystick%
        
        elif rt > 0:
            rotateRight()
            p1.ChangeDutyCycle(rt)#Set the P1 pulse signal duty cycle to the value of y joystick%
            p2.ChangeDutyCycle(rt)#Set the P2 pulse signal duty cycle to y joystick%

        

        




#some of the following code is taken from https://github.com/Cokoino/CKK0018/blob/main/Tutorial/Code/Drive_4_motors_run.py

#define the pin for drv8833#1
NSLEEP1 = 12  #Enabling signal pin for drv8833
AN11 = 17
AN12 = 27
BN11 = 22
BN12 = 23
#define the pin for drv8833#2
NSLEEP2 = 13
AN21 = 24
AN22 = 25
BN21 = 26
BN22 = 16
temp1=1


GPIO.setmode(GPIO.BCM)
#Define pin as output signal
GPIO.setup(NSLEEP1,GPIO.OUT)
GPIO.setup(NSLEEP2,GPIO.OUT)
GPIO.setup(AN11,GPIO.OUT)
GPIO.setup(AN12,GPIO.OUT)
GPIO.setup(BN11,GPIO.OUT)
GPIO.setup(BN12,GPIO.OUT)
GPIO.setup(AN21,GPIO.OUT)
GPIO.setup(AN22,GPIO.OUT)
GPIO.setup(BN21,GPIO.OUT)
GPIO.setup(BN22,GPIO.OUT)
#Initialize the motor drive signal so that the motor is in a stopped state
GPIO.output(AN11,GPIO.LOW)
GPIO.output(AN12,GPIO.LOW)
GPIO.output(BN11,GPIO.LOW)
GPIO.output(BN12,GPIO.LOW)
GPIO.output(AN21,GPIO.LOW)
GPIO.output(AN22,GPIO.LOW)
GPIO.output(BN21,GPIO.LOW)
GPIO.output(BN22,GPIO.LOW)
p1=GPIO.PWM(NSLEEP1,1000)#Define p1 as a pulse signal of 1000 Hz
p2=GPIO.PWM(NSLEEP2,1000)#Define p2 as a pulse signal of 1000 Hz

#p1 and p2 control motor speeds. i guess two motors are always the same?
p1.start(30)#P1 defaults to a duty cycle of 30%
p2.start(30)#P2 defaults to a duty cycle of 30%


#create code loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    main()    