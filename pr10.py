
# pip install adafruit-circuitpython-ads1x15 matplotlib numpy
# pip install adafruit-circuitpython-ads1x15
# pip install matplotlib numpy


import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# ========== ADS1115 Configuration ==========
i2c = busio.I2C(board.SCL, board.SDA)  # I2C bus
ads = ADS.ADS1115(i2c)                 # Create ADS object
ads.gain = 1                            # Input range ±4.096V
chan = AnalogIn(ads, ADS.P0)           # Use channel A0

# ========== Plot Settings ==========
plt.style.use("ggplot")
fig, ax = plt.subplots()

x_len = 200        # Number of points shown at a time
y_range = 5.0      # Y-axis range ±5V
xs = list(range(0, x_len))
ys = [0] * x_len   # Start with empty data

line, = ax.plot(xs, ys, color="blue")
ax.set_ylim(-y_range, y_range)
ax.set_title("Oscilloscope Demo - ADS1115 + Raspberry Pi")
ax.set_xlabel("Samples")
ax.set_ylabel("Voltage (V)")

# ========== Update Function ==========
def animate(i, ys):
    voltage = chan.voltage       # Read voltage
    ys.append(voltage)           # Add new sample
    ys = ys[-x_len:]             # Keep last x_len samples
    line.set_ydata(ys)           # Update plot
    return line,

# ========== Run Animation ==========
ani = animation.FuncAnimation(
    fig, animate, fargs=(ys,), interval=20, blit=True
)

plt.tight_layout()
plt.show()




## final code 
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# ========== ADS1115 Configuration ==========
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
ads.gain = 1  # ±4.096V input range
chan = AnalogIn(ads, ADS.P0)

# ========== Plot Settings ==========
plt.style.use("ggplot")
fig, ax = plt.subplots()

x_len = 200         # Number of points shown at a time
xs = list(range(0, x_len))
ys = [0] * x_len    # Start with empty data
line, = ax.plot(xs, ys, color="blue")

ax.set_ylim(-5, 5)  # initial Y-axis range
ax.set_title("Raspberry Pi ADS1115 - Oscilloscope")
ax.set_xlabel("Samples")
ax.set_ylabel("Voltage (V)")

# Text box to show live voltage
text_voltage = ax.text(0.02, 0.95, "", transform=ax.transAxes)

# Pause control
paused = False
def toggle_pause(event):
    global paused
    if event.key == " ":  # Spacebar toggle
        paused = not paused
        print("Paused" if paused else "Resumed")

fig.canvas.mpl_connect("key_press_event", toggle_pause)

# ========== Update Function ==========
def animate(i, ys):
    global paused
    if not paused:
        voltage = chan.voltage
        ys.append(voltage)
        del ys[:-x_len]  # keep only last x_len samples

        line.set_ydata(ys)
        text_voltage.set_text(f"Voltage: {voltage:.3f} V")

        # Auto-scale Y-axis
        ax.set_ylim(min(ys) - 0.5, max(ys) + 0.5)

    return line, text_voltage

# ========== Run Animation ==========
ani = animation.FuncAnimation(fig, animate, fargs=(ys,), interval=20, blit=True)
plt.tight_layout()
plt.show()
