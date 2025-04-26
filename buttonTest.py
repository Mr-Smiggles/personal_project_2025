from gpiozero import Button

button.wait_for_press(2)

button.wait_for_press()
print("Button pressed")