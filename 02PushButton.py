import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

button_pin=2
led_state=False
led_pin=3

GPIO.setup(button_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin,GPIO.OUT)

while True:
    if GPIO.input(button_pin)==GPIO.LOW:
        led_state=not led_state
        GPIO.output(led_pin,led_state)
        time.sleep(0.3)