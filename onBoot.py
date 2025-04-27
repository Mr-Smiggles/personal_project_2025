import os
from time import sleep
from gpiozero import Button

redButton = Button(21)
yellowButton = Button(20)
greenButton = Button(16)

os.system('python /home/jason/personal_project_2025/jcar.py')

def restartJCar():
    output = os.popen('ps -aux | grep python').read()
    if 'jcar.py' not in output:
        os.system('python /home/jason/personal_project_2025/jcar.py')

def buttonPressed():
    if redButton.is_pressed:
        os.system('pkill -f jcar.py')
        os.system('sudo shutdown now')
    if yellowButton.is_pressed:
        os.system('pkill -f jcar.py')
    if greenButton.is_pressed:
        os.system('pkill -f jcar.py')
        sleep(1)
        os.system('python /home/jason/personal_project_2025/jcar.py')
 

while True:
    restartJCar()
    buttonPressed()

