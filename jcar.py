import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Motor

#the following code is taken from https://github.com/Cokoino/CKK0018/blob/main/Tutorial/Code/Drive_4_motors_run.py
#my current theory is that these pin setups don't directly controll the motors, rather the motor controller chips on the hat.

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
p1.start(100)#P1 defaults to a duty cycle of 30%
p2.start(30)#P2 defaults to a duty cycle of 30%

#this should make all motors move 'foward' (needs to be correctly defined later). two should move at full speed and the other to at 30%
GPIO.output(AN11,GPIO.LOW)
GPIO.output(AN12,GPIO.HIGH)
GPIO.output(BN11,GPIO.LOW)
GPIO.output(BN12,GPIO.HIGH)
GPIO.output(AN21,GPIO.LOW)
GPIO.output(AN22,GPIO.HIGH)
GPIO.output(BN21,GPIO.LOW)
GPIO.output(BN22,GPIO.HIGH)
temp1=0