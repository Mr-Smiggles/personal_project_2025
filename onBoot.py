import os

#restart = open('restart.txt', 'r+')


def restartJCar():
    output = os.popen('ps -aux | grep python').read()
    if 'jcar.py' not in output:
        os.system('python /home/jason/personal_project_2025/jcar.py')
 

while True:
    restartJCar()
