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

def redButtonPressed():
    global doNotRestart
    doNotRestart = True
    print("Red button pressed")
    os.system('pkill -f jcar.py')
    os.system('sudo shutdown now')

def yellowButtonPressed():
    global doNotRestart
    doNotRestart = True
    print("Yellow button pressed")
    os.system('pkill -f jcar.py')

def greenButtonPressed():
    global doNotRestart
    doNotRestart = True
    print("Green button pressed")
    os.system('pkill -f jcar.py')
    sleep(5)
    doNotRestart = False
 
def buttonPressed():
    redButton.when_pressed = redButtonPressed
    yellowButton.when_pressed = yellowButtonPressed
    greenButton.when_pressed = greenButtonPressed

while True:
    restartJCar()
    buttonPressed()   
