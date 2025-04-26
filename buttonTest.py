import RPi.GPIO as GPIO
running = True

output = 1
redInput = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(output,GPIO.OUT)
GPIO.setup(redInput,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while running:
    print(f"Pin state: {GPIO.input(redInput)}")
    if GPIO.input(redInput) == GPIO.HIGH:
        print("Button Pushed!")
    else:
        GPIO.output(output,GPIO.LOW)
        print("Button Not Pushed!")