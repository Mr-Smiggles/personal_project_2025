import os
from gpiozero import Button


redButton = Button(2)

os.system('python /home/jason/personal_project_2025/jcar.py')

while True:
    if redButton.is_pressed:
        os.system('sudo shutdown now')
    else:
        print("Button is not pressed")