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

# nano index.md
# vim index.md

##3
# sudo apt install python3-pip
# pip3 install grip
# grip index.md


###
# [![Typora — a markdown editor, markdown reader.](https://tse2.mm.bing.net/th/id/OIP.VoqDm3kZU4HazLyb_k1r-gHaEf?pid=Api)](https://typora.io/?utm_source=chatgpt.com)

# Haan, **Typora** ek lightweight aur distraction-free Markdown editor hai jo Raspberry Pi par GUI (Graphical User Interface) mein achhe se kaam karta hai. Iska use karke aap apne `.md` (Markdown) files ko text aur images ke saath **properly render** kar sakte ho.

# ---

# ### Raspberry Pi par Typora kaise install karein?

# #### **Option 1: Snap Store se install karein**

# 1. **Snap support enable karein**:

#    ```bash
#    sudo apt update
#    sudo apt install snapd
#    sudo reboot
#    ```

# 2. **Typora install karein**:

#    ```bash
#    sudo snap install typora
#    ```

# 3. **Typora launch karein**:

#    * Menu se **Typora** search karke open karein.
#    * Ya terminal mein type karein:

#      ```bash
#      typora
#      ```

# **Note:** Snap packages thode heavy ho sakte hain, lekin ye installation ka sabse aasan tareeka hai.

# #### **Option 2: Official DEB package se install karein**

# 1. [Typora ke official website](https://typora.io/) par jaake **Linux (DEB)** version download karein.

# 2. Terminal mein navigate karke file ka path specify karein aur install karein:

#    ```bash
#    sudo dpkg -i typora-x.x.x.deb
#    sudo apt-get install -f
#    ```

# **Note:** Ye method thoda manual hai, lekin agar aapko Snap package nahi chahiye toh ye option use kar sakte hain.

# ---

# ### Typora ka use kaise karein?

# * **Text aur images render**: Typora mein aap jo likhte ho, wahi aapko real-time mein dikhta hai. Images ko drag-and-drop ya Markdown syntax se add kar sakte ho.

# * **Themes aur customization**: Typora mein built-in themes hain. Aap **Preferences** mein jakar theme change kar sakte ho.

# * **Export options**: Typora se aap apne documents ko PDF, HTML, Word, ya RTF format mein export kar sakte ho.

# ---

# ### 

# Agar aapko sirf `.md` file ko render karna hai bina editor ke, toh aap **Grip** tool ka use kar sakte ho:

# 1. Grip install karein:

#    ```bash
#    sudo apt install grip
#    ```

# 2. File ko render karein:

#    ```bash
#    grip index.md
#    ```

# 3. Browser mein open karein:

#    ```bash
#    xdg-open http://localhost:6419
#    ```

# Isse aap apne Markdown file ko browser mein dekh sakte ho bina kisi editor ke.

# ---

# Agar aap chahen, toh main aapko **Typora ka step-by-step guide** ya **Markdown syntax cheat sheet** bhi provide kar sakta hoon.



