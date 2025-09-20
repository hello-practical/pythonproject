import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

button=2
led_state=False
led=3

GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(led,GPIO.OUT)

while True:
    if GPIO.input(button)==GPIO.LOW:
        led_state=not led_state
        GPIO.output(led,led_state)
        time.sleep(0.3)   