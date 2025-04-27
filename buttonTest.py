from gpiozero import Button


redButton = Button(21)
yellowButton = Button(20)
greenButton = Button(18)

def redButtonPressed():
    print("Red button pressed")

def yellowButtonPressed():
    print("Yellow button pressed")

def greenButtonPressed():
    print("Green button pressed")
# while True:
#     if redButton.is_pressed:
#         print("Red button pressed")
#     if yellowButton.is_pressed:
#         print("Yellow button pressed")
#     if greenButton.is_pressed:
#         print("Green button pressed")
#     else:
#         pass

while True:
    redButton.when_pressed = redButtonPressed
    yellowButton.when_pressed = yellowButtonPressed
    greenButton.when_pressed = greenButtonPressed