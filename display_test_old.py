import random
import xpt2046
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

touch = xpt2046.Touch(spi, cs=digitalio.DigitalInOut(T_CS_PIN))
interrupt = digitalio.DigitalInOut(T_IRQ_PIN)
interrupt.direction = digitalio.Direction.INPUT


# Main loop:
try:
    # Clear the screen.
    display.fill(color565(0, 0, 0))
        
    while True:
        # Check if we have an interrupt signal
        print("e")
        if not interrupt.value:
            print("int")
            # Check where the pointer is
            spi.try_lock()
            spi.configure(baudrate = 100000)
            spi.unlock()
            if spi.frequency != 100000:
                raise Exception(spi.frequency)
            res = touch.raw_touch()

            if res is not None:
                x, y = touch.normalize(*res)
                print(res)
                y = 320 - y

                display.fill_rectangle(max(0, x - 10), max(0, y - 10), 20, 20, color565(255, 255, 255))

        # Delay for a bit
        time.sleep(0.05)

except KeyboardInterrupt:
    led.value = False
