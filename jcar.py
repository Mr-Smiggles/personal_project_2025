import RPi.GPIO as GPIO
import pygame
from time import sleep
running = True

pygame.init()
#setup controller

#initialize controller
for event in pygame.event.get():
    if event.type == pygame.JOYDEVICEADDED:
        print(event)
        controller = pygame.joystick.Joystick(event.device_index)
        controller.init()  # Initialize the joystick
    elif event.type == pygame.QUIT:
        running = False

#get left joystick raw x and y values
if controller.get_init():  # Check if the controller is initialized
   
        #get left joystick raw x and y values
        while running:
            controllerX = controller.get_axis(1) * -100  # gets left joystick x-axis
            controllerY = controller.get_axis(0) * 100  # gets left joystick y-axis

    #applies controller deadzone
            if controllerX >= 5 or controllerX <= -5:
                x = controllerX
            else:
                x = 0

            if controllerY >= 5 or controllerY <= -5:
                y = controllerY
            else:
                y = 0
            
            print(x, y)    

        
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

#the following code assumes that a negative voltage cannot be applied to spin the motor in the opposite direction

#this if statement should take care of foward and reversal of the motors with the joystick


def goFoward():
    GPIO.output(AN11,GPIO.LOW)
    GPIO.output(AN12,GPIO.HIGH)
    GPIO.output(BN11,GPIO.LOW)
    GPIO.output(BN12,GPIO.HIGH)
    GPIO.output(AN21,GPIO.LOW)
    GPIO.output(AN22,GPIO.HIGH)
    GPIO.output(BN21,GPIO.LOW)
    GPIO.output(BN22,GPIO.HIGH)
    

# def goBackward():
#         GPIO.output(AN11,GPIO.HIGH)
#         GPIO.output(AN12,GPIO.LOW)
#         GPIO.output(BN11,GPIO.HIGH)
#         GPIO.output(BN12,GPIO.LOW)
#         GPIO.output(AN21,GPIO.HIGH)
#         GPIO.output(AN22,GPIO.LOW)
#         GPIO.output(BN21,GPIO.HIGH)
#         GPIO.output(BN22,GPIO.LOW)
#         p1.ChangeDutyCycle(-y)#Set the P1 pulse signal duty cycle to the value of y joystick%
#         p2.ChangeDutyCycle(-y)#Set the P2 pulse signal duty cycle to y joystick%

# def determineDirection():
#     if y >= 0:
#         goFoward()
#     elif y < 0:
#         goBackward()

    #the follwoing code should spin the left & right motors opposite with the x joystick value
   
#create code loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    p1.ChangeDutyCycle(y)#Set the P1 pulse signal duty cycle to the value of y joystick%
    p2.ChangeDutyCycle(y)#Set the P2 pulse signal duty cycle to y joystick%