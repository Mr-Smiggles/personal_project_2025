from gpiozero import Button


redButton = Button(21)
yellowButton = Button(20)
greenButton = Button(12)


while True:
    if redButton.is_pressed:
        print("Red button pressed")
    if yellowButton.is_pressed:
        print("Yellow button pressed")
    if greenButton.is_pressed:
        print("Green button pressed")
    else:
        pass