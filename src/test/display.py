import random
import xpt2046_circuitpython
import time
import busio
import digitalio
from board import SCK, MOSI, MISO, D5, D6, D22, D23, D24, D25

from adafruit_rgb_display import color565
import adafruit_rgb_display.ili9341 as ili9341


# Configuration for CS and DC pins:
CS_PIN = D5
DC_PIN = D25
LED_PIN = D23
RST_PIN = D24

T_CS_PIN = D6
T_IRQ_PIN = D22

# Setup SPI bus using hardware SPI:
spi = busio.SPI(clock=SCK, MOSI=MOSI, MISO=MISO)

led = digitalio.DigitalInOut(LED_PIN)
led.direction = digitalio.Direction.OUTPUT
led.value = True

# Create the ILI9341 display:
display = ili9341.ILI9341(spi, cs=digitalio.DigitalInOut(CS_PIN),
                          dc=digitalio.DigitalInOut(DC_PIN), 
                          rst=digitalio.DigitalInOut(RST_PIN))

touch = xpt2046_circuitpython.Touch(spi, cs=digitalio.DigitalInOut(T_CS_PIN), interrupt=digitalio.DigitalInOut(T_IRQ_PIN))


# Main loop:
try:
    # Clear the screen.
    display.fill(color565(0, 0, 0))
        
    while True:
        # Check if we have an interrupt signal
        if touch.is_pressed():
            x, y = touch.get_coordinates()
            y = touch.height - y

            display.fill_rectangle(max(0, x - 10), max(0, y - 10), 20, 20, color565(255, 255, 255))

        # Delay for a bit
        time.sleep(0.1)

except KeyboardInterrupt:
    led.value = False