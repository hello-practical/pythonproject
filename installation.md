INSTALLATION Guide for IOT Practical


Practical 2
INPUT OUTPUT INTERFACE -
RPi GPIO BCM




Practical 3. 4 digit 7 segment display

The header file tm1637.py is already available on RPi (in /home/pi folder. Save your code in same folder.)

First try the import then add code

from time import sleep
import tm1637

Try:
import thread
except ImportError:
import _thread as thread
# Initialize the clock (GND, VCC=3.3V, Example Pins are DIO -20 and CLK21)

Display = tm1637.TM1637(CLK=21, DIO=20, brightness=1.0)


Practical 4: Using Telegram app for IOT

Installation : 

Ensure python is installed in latest version
python3.11 --version
Create and activate virtual environment
pip install telepot
To check if telepot is installed
pip list
Install telegram-bot for python 3.11
pip install python-telegram-bot
pip install gpiozero RPi.GPIO

Test code

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello from your bot!")

app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()


Practical 5 : Use RFID tag to control entry

Installation : 

Sudo apt install python3.11-venv
Python3.11 -m venv rfidenv
Source rfidenv/bin/activate

Pip install pyserial

Check the device terminal -

ls /dev/ttyUSB*

To install mysql (mariadb for RPi)

Activate virtual environment

pip install mysql-connector-python
sudo apt install update
sudo apt install mariadb-server

sudo mariadb

Mariadb environment will be loaded. Perform database action such as create db, table etc.

Practical 6 : Use of R307S fingerprint scanner

Connection diagram -



Installation

No installation. Save your python code in same directory as that of PyFingerprint. Do not create virtual environment.

Connect USB to serial converter to USB port of RPi.
Check the device terminal -

ls /dev/ttyUSB*


Practical 7 :  Capturing Images using RPi and USB camera

Enable camera, enable i2c interface, reboot

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



Practical 8 : GPIO control using MQTT client and server

Installation 
Create and activate virtual environment
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

Install MQTT and GPIO libraries
sudo apt update
sudo apt install mosquitto mosquitto-clients python3-pip -y
pip3 install paho-mqtt RPi.GPIO

Create a directory in /home/pi for this project.create python file - led_mqtt.py

To develop web application
We need to use flask framework to publish MQTT messages.Backend publishes "on" or "off" to home/led topic.

Installation 
pip3 install flask paho-mqtt

Create HTML template
In /home/pi/templates, create a file index. html. 
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
Signal input (e.g., waveform) unconnected for now
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


OTHER PROGRAMS - 
APPLYING INPUT (NOT DONE, NOT EXPECTED IN EXAM)
