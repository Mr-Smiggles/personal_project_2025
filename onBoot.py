import os
from time import sleep
from gpiozero import Button


redButton = Button(21)
yellowButton = Button(20)
greenButton = Button(18)

os.system('python3 /home/jason/personal_project_2025/jcar.py')

while True:
    if redButton.is_pressed:
        os.system('pkill -f jcar.py')
        print("Red button pressed")
        os.system('sudo shutdown now')
    if yellowButton.is_pressed:
        os.system('sudo pkill -f jcar.py')
        print("Yellow button pressed")
    if greenButton.is_pressed:
        os.system('pkill -f jcar.py')
        print("Green button pressed")
        sleep(1)
        os.system('python /home/jason/personal_project_2025/jcar.py')
    else:
        print("Button is not pressed")