import os
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Button

clean = False
redButton = Button(21)
yellowButton = Button(20)
greenButton = Button(16)

os.system('python /home/jason/personal_project_2025/jcar.py')

def gpioCleanup():
    output = os.popen('ps -aux | grep python').read()
    if 'jcar.py' in output:
        print("jcar.py is running", end='\r')
    else:
        GPIO.cleanup()
        clean = True

while True:
    gpioCleanup()
    if clean:
        redButton = Button(21)
        yellowButton = Button(20)
        greenButton = Button(16)
        clean = False
    else:
        continue

    if redButton.is_pressed:
        os.system('pkill -f jcar.py')
        os.system('sudo shutdown now')
    if yellowButton.is_pressed:
        os.system('pkill -f jcar.py')
    if greenButton.is_pressed:
        os.system('pkill -f jcar.py')
        sleep(1)
        os.system('python /home/jason/personal_project_2025/jcar.py')
    else:
        print("Button is not pressed")