import os
from time import sleep
from gpiozero import Button
import subprocess

jcar_process = None
doNotRestart = False
redButton = Button(21)
yellowButton = Button(20)
greenButton = Button(18)


def restartJCar():
    global doNotRestart
    global jcar_process


    if not doNotRestart:
        output = os.popen('ps -aux | grep python').read()

        if 'jcar.py' not in output:
            if jcar_process is None or not None:
                jcar_process = subprocess.Popen(['python', '/home/jason/personal_project_2025/jcar.py'], start_new_session=True)
        #os.system('python /home/jason/personal_project_2025/jcar.py')

def redButtonPressed():
    global doNotRestart
    doNotRestart = True
    print("Red button pressed")
    subprocess.run(['pkill', '-f', 'onBoot2.py'])
    subprocess.run(['pkill', '-f', 'python3 /home/jason/personal_project_2025/jcar.py'])
    subprocess.run(['sudo', 'shutdown', 'now'])

def yellowButtonPressed():
    global doNotRestart, jcar_process
    doNotRestart = True
    print("Yellow button pressed")
    if jcar_process:
        jcar_process.terminate()
        jcar_process = None

def greenButtonPressed():
    global doNotRestart
    doNotRestart = True
    print("Green button pressed")
    subprocess.run(['pkill', '-f', 'jcar.py'])
    sleep(5)
    doNotRestart = False
 
redButton.when_pressed = redButtonPressed
yellowButton.when_pressed = yellowButtonPressed
greenButton.when_pressed = greenButtonPressed

while True:
    restartJCar()
    print(doNotRestart)
    sleep(1)