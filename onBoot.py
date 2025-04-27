import os
from time import sleep
from gpiozero import Button


redButton = Button(40)
yellowButton = Button(38)
greenButton = Button(36)

os.system('python /home/jason/personal_project_2025/jcar.py')

while True:
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