from gpiozero import Button
from time import sleep
import os
import subprocess


redButton = Button(21)
yellowButton = Button(20)
greenButton = Button(18)


def redButtonPressed():
    print("Red button pressed")
    os.system('pkill -f onBoot.py')
    os.system('pkill -f jcar.py')
    os.system('sudo shutdown now')

def yellowButtonPressed():
    print("Yellow button pressed")
    os.system('pkill -f onBoot.py')
    os.system('pkill -f jcar.py')

def greenButtonPressed():
    print("Green button pressed")
    os.system('pkill -f onBoot.py')
    os.system('pkill -f jcar.py')
    sleep(5)
    os.system('python /home/jason/personal_project_2025/onBoot.py')
 


while True:
    redButton.when_pressed = redButtonPressed
    yellowButton.when_pressed = yellowButtonPressed
    greenButton.when_pressed = greenButtonPressed    
