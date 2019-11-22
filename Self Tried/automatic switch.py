import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

LEDPin = 26

buttonPin = 5

#Setup the pin the LED is connected to

GPIO.setup(LEDPin, GPIO.OUT)

# Setup the button
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

buttonPress = True
ledState = False

while(1):
            print("Press it")
            buttonPress = GPIO.input(buttonPin)
            if buttonPress == False and ledState ==False:
                        GPIO.output(LEDPin, True)
                        print("LED ON")
                        ledState = True
                        sleep(.25)
            elif buttonPress == False and ledState == True:
                        GPIO.output(LEDPin, True)
                        ledState = False
                        sleep(.25)

            sleep(0.15)
