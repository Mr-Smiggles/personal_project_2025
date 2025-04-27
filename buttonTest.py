from gpiozero import Button

redButton = Button(40)
yellowButton = Button(38)
greenButton = Button(36)

while True:
    if redButton.is_pressed:
        print("Red button pressed")
    if yellowButton.is_pressed:
        print("Yellow button pressed")
    if greenButton.is_pressed:
        print("Green button pressed")