##
# Create a directory in /home/pi for this project.create python file - led_mqtt.py

# Program to test publisher - subscriber model to control RPi GPIO
# Code - 

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

LED_PIN = 17

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("/home/led", qos=1)

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Received: {message}")
    if message.lower() == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
    elif message.lower() == "off":
        GPIO.output(LED_PIN, GPIO.LOW)

# MQTT client setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Run forever
try:
    client.loop_forever()
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nClean Exit")



## flask 

# Create flask application
# Python code -

from flask import Flask, render_template, request, redirect
import paho.mqtt.publish as publish

app = Flask(__name__)

MQTT_BROKER = "localhost"
MQTT_TOPIC = "home/led"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led/<state>')
def led_control(state):
    if state in ['on', 'off']:
        publish.single(MQTT_TOPIC, payload=state, hostname=MQTT_BROKER)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Create HTML template
# In /home/pi/templates, create a file index. html. Write following -

# <!DOCTYPE html>
# <html>
# <head>
#     <title>LED Control</title>
# </head>
# <body style="text-align:center; font-family:sans-serif;">
#     <h1>LED Control Panel</h1>
#     <form action="/led/on">
#         <button type="submit" style="padding:20px; font-size:20px;">Turn LED ON</button>
#     </form>
#     <br>
#     <form action="/led/off">
#         <button type="submit" style="padding:20px; font-size:20px;">Turn LED OFF</button>
#     </form>
# </body>
# </html>
