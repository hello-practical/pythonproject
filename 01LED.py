import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
while True :
    GPIO.output(3,True)
    time.sleep(1)
    GPIO.output(3,False)
    time.sleep(1)
    
    
# Multiple led blinking 

"""


import RPi.GPIO as GPIO
import time

# Set up the GPIO mode to use physical pin numbers
GPIO.setmode(GPIO.BOARD)

# Set up pins 3, 5, 7, and 11 as output pins for the LEDs
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

# Infinite loop to blink the LEDs
try:
    while True:
        # Turn all LEDs on
        GPIO.output(3, True)
        GPIO.output(5, True)
        GPIO.output(7, True)
        GPIO.output(11, True)
        time.sleep(1)

        # Turn all LEDs off
        GPIO.output(3, False)
        GPIO.output(5, False)
        GPIO.output(7, False)
        GPIO.output(11, False)
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO settings when exiting the program
    GPIO.cleanup()

"""


# Buzzer
"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(3, GPIO.OUT)  # Pin 3 on the Raspberry Pi board (physical pin 3)

while True:
    GPIO.output(3, True)  # Turn LED on
    time.sleep(1)  # Wait for 1 second
    GPIO.output(3, False)  # Turn LED off
    time.sleep(1)  # Wait for 1 second
    

"""