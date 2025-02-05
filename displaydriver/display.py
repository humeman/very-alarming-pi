import asyncio
from typing import List, Optional
from displaydriver.screen import Screen
from displaydriver.colors import Colors
import displayio
import xpt2046
import digitalio
import time

class Display:
    def __init__(
            self, 
            display: displayio.Display, 
            touch: xpt2046.Touch,
            interrupt: digitalio.DigitalInOut,
            interrupt_direction: bool,
            touch_normalizer: Optional[callable] = None):
        """
        Initializes the display graphics driver.
        
        Args:
            display: An initialized DisplayIO display instance.
                At this time, this will only work with 565-encoded SPI bus displays.
            touch: An initialized Touch interface instance.
            interrupt: A DigitalIO pin which can be configured as an interrupt. Indicates
                that the screen has been touched.
            interrupt_direction: The pin state which indicates a touch has occurred
                on the interrupt pin.
            touch_normalizer: A function that takes in X, Y coordinates as input
                and normalizes them to the actual screen coordinates (as desired).
                Can be used as a calibration method.
        """
        self._display = display
        self._display.auto_refresh = False
        self._group = displayio.Group()
        self._display.root_group = self._group
        self._touch = touch
        self._interrupt = interrupt
        self._interrupt_direction = interrupt_direction
        self._background_color = Colors.BLACK
        self._screen: Screen = None
        self._touch_normalizer = touch_normalizer
        self.width = self._display.width
        self.height = self._display.height
        
    async def loop(self) -> None:
        """
        Runs the async loop for this display, which will handle button presses,
        call periodic tasks, and redraw the display as necessary.
        """
        last_int = 0
        
        while True:
            if self._interrupt.value == self._interrupt_direction:
                if last_int < time.time_ns() - 300 * 1_000_000:
                    self._handle_interrupt()
                    last_int = time.time_ns()
                
            if self._screen.tick():
                self._draw_frame()
            await asyncio.sleep(0)
        
    def set_screen(self, screen: Screen) -> None:
        """
        Changes the active screen to be rendered.
        
        Args:
            screen: The new active screen.
        """
        if self._screen is not None:
            for element in self._group.get_displayio_elements():
                self._group.remove(element)
        self._screen = screen
        for element in self._screen.get_displayio_elements():
            self._group.append(element)
        self._draw_frame()
        
    def set_background_color(self, color: int) -> None:
        """
        Changes the background color, filled on each frame.
        Args:
            color: An RGB color (ie, 0x00FF00 = green).
                Use colors.Colors (ie, Colors.BLACK) for basic colors.
        """
        self._background_color = color
        self._draw_frame()
        
    def _handle_interrupt(self) -> None:
        self._touch.spi.try_lock()
        self._touch.spi.configure(baudrate = 100000)
        self._touch.spi.unlock()
        if self._touch.spi.frequency != 100000:
            raise Exception(self._touch.spi.frequency)
        val = None
        count = 0
        while val is None and count < 5:
            val = self._touch.raw_touch()

        if val is None:
            return # better to skip here than error
        
        x, y = self._touch.normalize(*val)
        if self._touch_normalizer is not None:
            x, y = self._touch_normalizer(x, y)
        
        if self._screen is not None:
            self._screen.handle_click(x, y)

        self._draw_frame()
        
    def _draw_frame(self) -> None:
        self._display.refresh()