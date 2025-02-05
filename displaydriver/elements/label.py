from typing import Optional
from displaydriver.colors import Colors
from displaydriver.display import Display
from displaydriver.ui import UIElement
import displayio
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
import fontio

class Label(UIElement):
    def __init__(
            self, 
            display: Display,
            font: fontio.FontProtocol,
            x: int, 
            y: int, 
            text: str, 
            color: int = Colors.WHITE,
            scale: int = 1,
            tick: Optional[callable] = None) -> None:
        self._label = label.Label(
            font,
            text = text,
            color = color,
            scale = scale
        )
        self._scale = scale
        self._display = display
        self.set_location(x, y)
        self._tick = tick
        
    def set_location(self, x, y):
        self._label.x = x if x >= 0 else self._display.width // 2 - self._label.width * self._scale // 2
        self._label.y = y if y >= 0 else self._display.height // 2 - self._label.height * self._scale // 2
        
    def get_displayio_elements(self):
        return [self._label]
    
    def handle_click(self, x, y):
        pass
    
    def tick(self):
        if self._tick is not None:
            return self._tick(self)
        return False