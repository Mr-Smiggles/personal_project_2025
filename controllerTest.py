import pygame
pygame.init()
running = True

#controller

#initialize controller
for event in pygame.event.get():
    if event.type == pygame.JOYDEVICEADDED:
        print(event)
        controller = pygame.joystick.Joystick(event.device_index)
        controller.init()  # Initialize the joystick
    elif event.type == pygame.QUIT:
        running = False

def getLeftAxes():
    if controller.get_init():  # Check if the controller is initialized
   
        #get left joystick raw x and y values
        controllerX = controller.get_axis(1) * -100  # gets left joystick x-axis
        controllerY = controller.get_axis(0) * 100  # gets left joystick y-axis
        controllerLT = controller.get_axis(2) * 100
        controllerRT = controller.get_axis(5) * 100

        #applies controller deadzone
        if controllerX >= 5 or controllerX <= -5:
            x = controllerX
        else:
            x = 0

        if controllerY >= 5 or controllerY <= -5:
            y = controllerY
        else:
            y = 0

        if controllerLT >= 5:
            lt = controllerLT

        else:
            lt = controllerLT - controllerLT
        
        print(x, y)

#create code loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    getLeftAxes()