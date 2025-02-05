from displaydriver.colors import Colors
from displaydriver.display import Display
from displaydriver.ui import UIElement
import displayio
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
from adafruit_display_shapes import rect
import fontio

class Button(UIElement):
    def __init__(
            self, 
            display: Display,
            font: fontio.FontProtocol,
            x: int, 
            y: int, 
            text: str, 
            color: int = Colors.WHITE,
            scale: int = 1,
            padding: int = 1) -> None:
        self._label = label.Label(
            font,
            text = text,
            color = color,
            scale = scale
        )
        self._label.anchor_point = (0, 0)
        self._label.anchored_position = (
            x if x >= 0 else display.width // 2 - self._label.width * scale // 2,
            y if y >= 0 else display.height // 2 - self._label.height * scale // 2
        )
        # These numbers do not make sense in any way whatsoever, and yet they work
        # Isn't that cool?
        self._rect_width = 2 * padding + self._label.width * scale + scale
        self._rect_height = 2 * padding + self._label.height * scale + scale
        self._rect_x = self._label.anchored_position[0] - scale - padding
        self._rect_y = self._label.anchored_position[1] - scale - padding
        self._rect = rect.Rect(
            x = self._rect_x,
            y = self._rect_y,
            width = self._rect_width,
            height = self._rect_height,
            fill = None,
            outline = color,
            stroke = scale
        )
        self._scale = scale
        self._display = display
        
    def get_displayio_elements(self):
        return [self._label, self._rect]
    
    def handle_click(self, x, y):
        if x >= self._rect_x and x <= self._rect_x + self._rect_width \
            and y >= self._rect_y and y <= self._rect_y + self._rect_height:
            print("Clicked!")
    
    def tick(self):
        return False