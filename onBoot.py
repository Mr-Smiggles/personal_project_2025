import os

output = os.popen('ps -aux | grep python').read()


if 'buttons.py' not in output:
    os.system('python /home/jason/personal_project_2025/buttons.py')


def restartJCar():
    global output
    if 'jcar.py' not in output:
        os.system('python /home/jason/personal_project_2025/jcar.py')


while True:
    restartJCar()
