import random
from typing import Tuple
import displaydriver.colors
import displaydriver.display
from displaydriver.elements.button import Button
from displaydriver.elements.label import Label
import displaydriver.screen
import xpt2046
import time
import busio
import digitalio
from board import SCK, MOSI, MISO, D5, D6, D22, D23, D24, D25
import displayio
import adafruit_ili9341 
from adafruit_bitmap_font import bitmap_font
import asyncio

import displaydriver


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
# Release any previously configured displays
displayio.release_displays()

# Create the ILI9341 display:
display_bus = displayio.FourWire(
    spi, command=DC_PIN, chip_select=CS_PIN, reset=RST_PIN
)
raw_display = adafruit_ili9341.ILI9341(display_bus, width=240, height=320, rotation = 90)
touch = xpt2046.Touch(spi, cs=digitalio.DigitalInOut(T_CS_PIN))
interrupt = digitalio.DigitalInOut(T_IRQ_PIN)
interrupt.direction = digitalio.Direction.INPUT

def touch_normalizer(x: int, y: int) -> Tuple[int, int]:
    return (raw_display.width - x, y)

display = displaydriver.display.Display(
    raw_display,
    touch,
    interrupt,
    False,
    touch_normalizer = touch_normalizer
)
points = []
font = bitmap_font.load_font("bitocra.pcf")
screen = displaydriver.screen.UIScreen()
global ctime
def tick(label):
    ntime = int(time.time())
    if label._ctime != ntime:
        label._label.text = str(ntime)
        label._ctime = ntime
        print(f"updated text: {label._label.text}")
        return True
    
    return False
label = Label(display, font, -1, 18, "Hello world!", color = displaydriver.colors.Colors.CYAN, scale = 3, tick = tick)
label._ctime = int(time.time())
button = Button(display, font, -1, 100, "CLICK ME!", color = displaydriver.colors.Colors.ORANGE, scale = 3, padding = 10)
screen.add_element(button)
button = Button(display, font, -1, 200, "right now.", color = displaydriver.colors.Colors.GREEN, scale = 2, padding = 5)
screen.add_element(label)
screen.add_element(button)
display.set_screen(screen)
loop = asyncio.new_event_loop()
loop.run_until_complete(display.loop())