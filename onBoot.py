import os
from time import sleep
from gpiozero import Button

doNotRestart = False
redButton = Button(21)
yellowButton = Button(20)
greenButton = Button(18)


def restartJCar():
    output = os.popen('ps -aux | grep python').read()
    if 'jcar.py' not in output and doNotRestart == False:
        os.system('python /home/jason/personal_project_2025/jcar.py')

def buttonPressed():
    if redButton.is_pressed:
        doNotRestart = True
        os.system('pkill -f jcar.py')
        os.system('sudo shutdown now')
    if yellowButton.is_pressed:
        doNotRestart = True
        os.system('pkill -f jcar.py')
    if greenButton.is_pressed:
        doNotRestart = True
        os.system('pkill -f jcar.py')
        sleep(5)
        doNotRestart = False
 

while True:
    restartJCar()
    buttonPressed()

