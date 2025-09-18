Study Guide for IOT Practical


Practical 2
Push Button Interface
https://www.hackster.io/hardikrathod/push-button-with-raspberry-pi-6b6928

Practical 3. 4 digit 7 segment display

This is a common anode 4-digit tube display module which uses the TM1637 driver chip; Only 2 connections are required to control the 4-digit 7-segment displays
Features of the module:
Display common anode for the four red LED
Powered supply by 3.3V/5V
Four common anode tube display module is driven by IC TM1637
Can be used for Arduino devices or raspberry pi boards, two signal lines can make the MCU control 4 8 digital tube. Digital tube 8 segment is adjustable
Here is how to hook the module up

The header file tm1637.py is already available on RPi (in /home/pi folder. Save your code in same folder.)

First try the import then add code

To display Real time clock

from time import sleep
import tm1637

Try:
import thread
except ImportError:
import _thread as thread
# Initialize the clock (GND, VCC=3.3V, Example Pins are DIO -20 and CLK21)

Display = tm1637.TM1637(CLK=21, DIO=20, brightness=1.0)
Try:
print ("Starting clock in the background (press CTRL + C to stop):")
Display.StartClock(military_time=True)
Display.SetBrightness(1.0)
while True:
Display.ShowDoublepoint(True)
sleep(1)
Display.ShowDoublepoint(False)
sleep(1)
Display.StopClock()
thread.interrupt_main()
except KeyboardInterrupt:
print ("Properly closing the clock and open GPIO pins")
Display.cleanup()

Other programs - Display a digital counter ‘0000 - 9999’ ; Display a string ‘RJIT’


Practical 4: Using Telegram app for IOT

No Connections

Installation : 

Ensure python is installed in latest version
python3.11 --version
If not found install python venv package
sudo apt install python3.11-venv

Create virtual environment
python3 -m venv envName

Activate the virtual environment
source envName/bin/activate

Install telepot
pip install telepot

To check if telepot is installed
pip list


Install telegram-bot for python 3.11
pip install python-telegram-bot

Inside virtual environment install gpiozero
pip install gpiozero RPi.GPIO

In mobile telegram application, create a new bot. Generate token and note down the token.

First write and test imports then write and execute code

Test code

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello from your bot!")

app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

Once test code is successful, bot can be used to control GPIO. (LED or any device connected to GPIO

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import RPi.GPIO as GPIO

# Use BCM numbering
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

def on_led(update: Update, ctx: CallbackContext):
    GPIO.output(LED_PIN, GPIO.HIGH)
    update.message.reply_text("LED is ON")

def off_led(update: Update, ctx: CallbackContext):
    GPIO.output(LED_PIN, GPIO.LOW)
    update.message.reply_text("LED is OFF")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("on", on_led))
    dp.add_handler(CommandHandler("off", off_led))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

GPIO Connections as per practical 2

Other programs - control various output devices like LEDs, buzzers etc.

Practical 5 : Use RFID tag to control entry

Installation : 

Sudo apt install python3.11-venv
Python3.11 -m venv rfidenv
Source rfidenv/bin/activate
Pip install pyserial

Connect EM18 to USB to Serial Connector
EM18		USB to Serial
GND	- 	GND
+5V		+5V
 Tx		  Rx

Connect USB to serial converter to USB port of RPi.
Check the device terminal -

ls /dev/ttyUSB*

Program to read and print RFID tag data

Code

import serial
def rfid_read():
	try:
		ser=serial.Serial(‘/dev/ttyUSB0’, baudrate=9600, timeout =1)
		print(“Reading …”)
		while True:
			data=ser.read(12)
			if data:
				tag=data.decode(‘utf-8’).strip()
				print(f”RFID tag:{tag})
	Except Exception as e:
		print(f”Error:{e})
	finally:
		ser.close()
If __name__ ==”__main__”:
	read_rfid()

Other programs -
Print valid and Invalid RFID tags
Sounding a alarm (using buzzer) for invalid RFID tag
Saving Data in mysql database 
Menu driven python code for - Register new card, Mark Attendance, Delete card.


Installing mysql

Activate virtual environment

pip install mysql-connector-python
sudo apt install update
sudo apt install mariadb-server

sudo mariadb

-- Create DB
CREATE DATABASE rfid_db;

-- Create user (if not already exists)
DROP USER IF EXISTS 'rfid_user'@'localhost';
CREATE USER 'rfid_user'@'localhost' IDENTIFIED BY 'yourpassword';

-- Give access
GRANT ALL PRIVILEGES ON rfid_db.* TO 'rfid_user'@'localhost';
//FLUSH PRIVILEGES;

- Check if user is created
SELECT user,host FROM mysql.user

EXPECTED
rfid_user | localhost

-- Select DB
USE rfid_db;

-- Create table
CREATE TABLE rfid_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tag_id VARCHAR(50),
    timestamp DATETIME
);
Test code

import mysql.connector
print(“MySQL working”)

Code -

import serial
import mysql.connector
import datetime

def save_to_db(tag):
conn = mysql.connector.connect(
host=’localhost’,
user=’rfid_user’
password=’password’,
database=’rfid_db’)
cursor=conn.cursor()
sql=”INSERT INTO rfid_logs(tag_id, timestamp) VALUES (%s,%s)”
cursor.execute(sql,(tag,time.strftime(‘%Y-%m-%d %H:%M:%S’)))
conn.commit()
cursor.close()
conn.close()
print(f”saved tag: {tag}”)

def rfid_read():
	try:
		ser=serial.Serial(‘/dev/ttyUSB0’, baudrate=9600, timeout =1)
		print(“Reading …”)
		while True:
			data=ser.read(12)
			if data:
				tag=data.decode(‘utf-8’).strip()
				print(f”RFID tag:{tag})
				save_to_db(tag)

	Except Exception as e:
		print(f”Error:{e})
	finally:
		ser.close()
If __name__ ==”__main__”:
	read_rfid()


##
Modify above program to a menu driven python script -
New entry
Attendance

save_to_db(tag) will work for New entry.
Write attendance() function to print attendance for the relevant tag.


Practical 6 : Use of R307S fingerprint scanner

Connection diagram -



Connections

USB to Serial Converter - VCC to VCC of FingerPrint scanner
USB to Serial Converter - GND to GND of FingerPrint scanner
USB to Serial Converter - RxD to TxD of FingerPrint scanner
USB to Serial Converter - TxD to RxD of FingerPrint scanner

Installation

No installation. Save your python code in same directory as that of PyFingerprint. Do not create virtual environment.

Connect USB to serial converter to USB port of RPi.
Check the device terminal -

ls /dev/ttyUSB*
Code : 

Test the fingerprint scanner to record a fingerprint. 
(assuming no previous fingerprint entries are available)

import time
from pyfingerprint.pyfingerprint import PyFingerprint
try:
	f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
except Exception as e:
	print('Exception message: ' + str(e))
	exit(1)

def enrollFinger():
	print('Waiting for finger...')
	while ( f.readImage() == False ):
		pass
	positionNumber = result[0]
print('Remove finger...')
	time.sleep(2)
	print('Waiting for same finger again...')
	while ( f.readImage() == False ):
		pass
	f.convertImage(0x02)
	if ( f.compareCharacteristics() == 0 ):
		print ("Fingers do not match")
		time.sleep(2)
		Return
	f.createTemplate()
	positionNumber = f.storeTemplate()
	print('Finger enrolled successfully!')
	print('New template position #' + str(positionNumber))
	time.sleep(2)

if __name__ == '__main__':
     enrollFinger()
    ## searchFinger()
    ## deleteFinger()

Other Programs

Enrol, Search and Delete fingers


Practical 7 :  Capturing Images using RPi and USB camera

Connection
USB Camera direct connection

ls /dev/video*

sudo apt update
sudo apt install v4l-utils

v4l2-ctl --list-devices

Camera should be visible in output

sudo apt install ffplay -y
ffplay /dev/video0


Install Packages

sudo apt update
sudo apt install python3-opencv python3-numpy libopencv-dev -y

Test camera using python
import cv2

# Open USB camera (usually /dev/video0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("USB Camera not detected")
    exit()

print("Press 'q' to quit the preview")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("USB Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

Other programs

To save a capture
To save multiple images (creation of dataset)


Practical 8 : GPIO control using MQTT client and server

Concept - 
An MQTT broker is a server that facilitates communication between clients using the MQTT protocol, which is designed for lightweight messaging in IoT applications. It receives messages from publishers and routes them to the appropriate subscribers based on topics.An MQTT broker is a server that facilitates communication between MQTT clients. It acts as an intermediary, receiving messages from clients (publishers) and routing them to the appropriate clients (subscribers) based on topics. This publish-subscribe model allows for efficient and scalable messaging, especially in Internet of Things (IoT) applications.


Create virtual environment
python3 -m venv envName

Activate the virtual environment
source envName/bin/activate
Installation 
sudo apt install mosquitto mosquitto-clients -y
Enable Broker 
sudo systemctl enable mosquitto
Test
Terminal 1- (subscriber)
Bash
Mosquitto_sub -h localhost -t test/topic
Terminal 2 (publisher)
Mosquitto_pub -h localhost -t test/topic -m “Hello!!”

Using MQTT to control GPIO

Concept -

A MQTT subscriber is used to listen for LED control messages. messages (like "on" or "off") are published from another terminal or device.

Install MQTT and GPIO libraries
sudo apt update
sudo apt install mosquitto mosquitto-clients python3-pip -y
pip3 install paho-mqtt RPi.GPIO

Create a directory in /home/pi for this project.create python file - led_mqtt.py

Program to test publisher - subscriber model to control RPi GPIO
Code - 

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

LED_PIN=17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code" + str(rc))
    client.subscribe("/home/led")

def on_message(client,userdata, msg):
    message=msg.payload.decode()
    print(f"received:{message}")
    if message== "on":
        GPIO.output(LED_PIN,GPIO.HIGH)
    elif message=="off":
        GPIO.output(LED_PIN,GPIO.LOW)
client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message

client.connect("localhost",1883,60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nClean Exit")

Run this code from the virtual environment 

(myenv) pi@raspberrypi:~/mqtt_led_proj $ python led_mqtt.py
/home/pi/mqtt_led_proj/led_mqtt.py:

23: DeprecationWarning: Callback API version 1 is deprecated, update to latest version
client=mqtt.Client()
Connected with result code0

To test the code with publisher - 
(myenv) pi@raspberrypi:~/mqtt_led_proj $ mosquitto_pub -h localhost -t /home/led -m "on"

This should turn ON or OFF the LED connected at GPIO 17 (pin no 11)

To develop web application
We need to use flask framework to publish MQTT messages.Backend publishes "on" or "off" to home/led topic.

Installation 
pip3 install flask paho-mqtt

Create flask application
Python code -

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

Create HTML template
In /home/pi/templates, create a file index. html. Write following -

<!DOCTYPE html>
<html>
<head>
    <title>LED Control</title>
</head>
<body style="text-align:center; font-family:sans-serif;">
    <h1>LED Control Panel</h1>
    <form action="/led/on">
        <button type="submit" style="padding:20px; font-size:20px;">Turn LED ON</button>
    </form>
    <br>
    <form action="/led/off">
        <button type="submit" style="padding:20px; font-size:20px;">Turn LED OFF</button>
    </form>
</body>
</html>

Run python application.
From web browser, hit http://<ip address of RPi>>:5000
Turn LED ON and OFF using interface.


Practical 9 : Configuration of Wireless Access Point

Setting up Raspberry pi as wireless access point.

Installation

sudo apt install hostapd dnsmasq -y

Stop the services to start with

sudo systemctl stop hostapd
sudo systemctl stop dnsmasq

Check network manager status
nmcli device status
Output expected
DEVICE      TYPE      STATE      CONNECTION
wlan0       wifi      disconnected  --
eth0        ethernet  connected    Wired connection 1

Create a Wi-Fi Hotspot Using NetworkManager

nmcli dev wifi hotspot ifname wlan0 ssid RPi3_AP password raspberry123

Verify Hotspot

nmcli connection show

To confirm DHCP is working:

nmcli dev show wlan0 | grep IP4

Sample output

IP4.ADDRESS[1]:    10.42.0.1/24
IP4.GATEWAY:       --

This ensures the setting of Wifi

Choice based program to start, stop and read status of hotspot.

Program to control hotspot -

import subprocess

def create_hotspot(ssid="RPi3_AP", password="raspberry"):
    subprocess.run([ "nmcli", "dev", "wifi", "hotspot", "ifname", "wlan0", "ssid", ssid, "password", password], check=True)
    print(f"Hotspot '{ssid}' created successfully!")

def stop_hotspot():
    # Find active hotspot
    result = subprocess.run(
        ["nmcli", "-t", "-f", "NAME,TYPE", "con", "show", "--active"], capture_output=True, text=True )
    for line in result.stdout.splitlines():
        if "wifi" in line:
            name = line.split(":")[0]
            subprocess.run(["nmcli", "con", "down", name], check=True)
            print(f"Hotspot '{name}' stopped.")

def status_hotspot():
    subprocess.run(["nmcli", "dev", "status"])

if __name__ == "__main__":
    print("1. Start Hotspot\n2. Stop Hotspot\n3. Status")
    choice = input("Select option: ").strip()
    if choice == "1":
        ssid = input("Enter SSID [default RPi3_AP]: ") or "RPi3_AP"
        password = input("Enter Password [default raspberry123]: ") or "raspberry123"
        create_hotspot(ssid, password)
    elif choice == "2":
        stop_hotspot()
    elif choice == "3":
        status_hotspot()
    else:
        print("Invalid choice!")

Other programs - to create the wifi hotspot, to start or to stop the wifi hotspot.


Practical 10 : Oscilloscope



Circuit Connections
ADS1115 uses I2C, so connect it like this:
ADS1115 Pin
Raspberry Pi 3 B+ Pin
VDD
3.3V (Pin 1)
GND
GND (Pin 6)
SDA
GPIO2 / SDA1 (Pin 3)
SCL
GPIO3 / SCL1 (Pin 5)
A0
Signal input (e.g., waveform)
A1, A2, A3
Optional inputs


Enable I2C on Raspberry Pi and reboot
Check if ADS1115 IS DETECTED
i2cdetect -y 1

Install Required Libraries

sudo apt update
sudo apt install python3-pip -y
pip3 install --break-system-packages --upgrade pip setuptools wheel

INSTALL PYTHON LIBRARIES

pip3 install --break-system-packages adafruit-circuitpython-ads1x15 matplotlib numpy

PROGRAM TO DEMONSTRATE OSCILLOSCOPE PLOT
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create ADS object
ads = ADS.ADS1115(i2c)
ads.gain = 1  # ±4.096V range

# Use channel 0 (AIN0)
chan = AnalogIn(ads, ADS.P0)

# Plot settings
plt.style.use('ggplot')
fig, ax = plt.subplots()
x_len = 200   # Number of points to display
y_range = 5.0  # ±4.096V max range
xs = list(range(0, x_len))
ys = [0] * x_len
line, = ax.plot(xs, ys)

ax.set_ylim(-y_range, y_range)
ax.set_title("Raspberry Pi ADS1115 Oscilloscope")
ax.set_xlabel("Samples")
ax.set_ylabel("Voltage (V)")

def animate(i, ys):
    # Read voltage from ADS1115
    voltage = chan.voltage
    ys.append(voltage)
    ys = ys[-x_len:]
    line.set_ydata(ys)
    return line,

ani = animation.FuncAnimation(fig, animate, fargs=(ys,), interval=20, blit=True)
plt.tight_layout()
plt.show()

OTHER PROGRAMS - 
APPLYING INPUT (NOT DONE, NOT EXPECTED IN EXAM)
