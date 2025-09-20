import tm1637
from time import sleep
import threading

# Initialize the display
Display = tm1637.TM1637(clk=21, dio=20, brightness=1.0)

try:
    print("Starting clock in the background (press CTRL + C to stop):")
    Display.StartClock(military_time=True)
    Display.SetBrightness(1.0)

    while True:
        Display.ShowDoublepoint(True)
        sleep(1)
        Display.ShowDoublepoint(False)
        sleep(1)

except KeyboardInterrupt:
    print("Properly closing the clock and open GPIO pins.")
    Display.StopClock()
    Display.cleanup()
