from gpiozero import Button

i = 0

redButton = Button(21)
yellowButton = Button(20)
greenButton = Button(16)


while True:
    if redButton.is_pressed:
        print("Red button pressed", i+1)
    if yellowButton.is_pressed:
        print("Yellow button pressed", i+1)
    if greenButton.is_pressed:
        print("Green button pressed", i+1)
    else:
        pass