from typing import Optional, Tuple, Union
from displaydriver.colors import Colors
import displayio
import numpy

# class DisplayGraphics:
#     def __init__(self, width: int, height: int):
#         """
#         Initializes the display graphics driver, an interface which provides
#         graphics methods on top of a DisplayIO bitmap.
        
#         Args:
#             bitmap: A DisplayIO bitmap in 565 colorspace.
#         """
#         self._width = width
#         self._height = height
#         self._bitmap = numpy.zeros((width, height), dtype = numpy.uint16)
#         self._dirty_x0 = None
#         self._dirty_x1 = None
#         self._dirty_y0 = None
#         self._dirty_y1 = None
        
#     def _mark_dirty(self, x: int, y: int) -> None:
#         if self._dirty_x0 is None:
#             self._dirty_x0 = x
#             self._dirty_x1 = x
#         else:
#             self._dirty_x0 = min(self._dirty_x0, x)
#             self._dirty_x1 = max(self._dirty_x1, x)
#         if self._dirty_y0 is None:
#             self._dirty_y0 = y
#             self._dirty_y1 = y
#         else:
#             self._dirty_y0 = min(self._dirty_y0, x)
#             self._dirty_y1 = max(self._dirty_y1, x)
            
#     def is_dirty(self) -> bool:
#         return self._dirty_x0 is not None
    
#     def get_dirty_0(self) -> Tuple[int, int]:
#         return (self._dirty_x0, self._dirty_y0)
    
#     def get_dirty_1(self) -> Tuple[int, int]:
#         return (self._dirty_x1, self._dirty_y1)
    
#     def iterate_dirty(self):
#         iterator = BitmapIterator(self._bitmap, self._dirty_x0, self._dirty_y0, self._dirty_x1, self._dirty_y1)
#         self._dirty_x0 = None
#         self._dirty_x1 = None
#         self._dirty_y0 = None
#         self._dirty_y1 = None
#         return iterator
        
#     def fill_screen(self, color: Union[int, Colors]) -> None:
#         """
#         Fills in the screen with a new color.
        
#         Args:
#             color: The new color for the screen.
#         """
#         if type(color) == Colors:
#             color = color.value
#         for x in range(0, self._width):
#             for y in range(0, self._height):
#                 self._bitmap[x, y] = GraphicsUtil.encode_color_565(color)
#         self._dirty_x0 = 0
#         self._dirty_x1 = self._width - 1
#         self._dirty_y0 = 0
#         self._dirty_y1 = self._height - 1
        
#     def point(self, x: int, y: int, color: int, alpha: Optional[float] = None) -> None:
#         """
#         Draws a single point to the display.
        
#         Args:
#             x: The X coordinate.
#             y: The Y coordinate.
#             color: The color of the point.
#             alpha: The alpha value of the point (optional -- default 100%).
#                 Must be 0 <= alpha <= 1.
#         """
#         if alpha is not None:
#             # Find the current pixel value
#             old_color = self._display.pixel(x, y)
            
#             # Our new color becomes the mixed value between those two
#             color = GraphicsUtil.mix_colors(old_color, color, alpha)
            
#         self._bitmap[x, y] = GraphicsUtil.encode_color_565(color)
#         self._mark_dirty(x, y)
        
#     def fill(self, x0: int, y0: int, x1: int, y1: int, color: int, alpha: Optional[float] = None) -> None:
#         """
#         Fills in an area with a new color.
        
#         Args:
#             x0: The X coordinate of the first corner (inclusive).
#             y0: The Y coordinate of the first corner (inclusive).
#             x1: The X coordinate of the second corner (inclusive).
#             y1: The Y coordinate of the second corner (inclusive).
#             color: The color of the area.
#             alpha: The alpha value of the area (optional -- default 100%).
#                 Must be 0 <= alpha <= 1.
#         """
#         low_x = min(x0, x1)
#         high_x = max(x0, x1)
#         x = low_x
#         low_y = min(y0, y1)
#         high_y = max(y0, y1)
        
#         while x <= high_x:
#             y = low_y
            
#             while y <= high_y:
#                 self.point(x, y, color, alpha)
#                 y += 1
                
#             x += 1
            
#     def horizontal_line(self, x0: int, x1: int, y: int, color: int, alpha: Optional[float] = None) -> None:
#         """
#         Draws a horizontal line with a color.
        
#         Args:
#             x0: The X coordinate of the start (inclusive).
#             x1: The X coordinate of the end (inclusive).
#             y: The Y coordinate of the line.
#             color: The color of the line.
#             alpha: The alpha value of the area (optional -- default 100%).
#                 Must be 0 <= alpha <= 1.
#         """
#         low = min(x0, x1)
#         high = max(x0, x1)
#         x = low
        
#         while x <= high:
#             self.point(x, y, color, alpha)
#             x += 1
            
#     def vertical_line(self, x: int, y0: int, y1: int, color: int, alpha: Optional[float] = None) -> None:
#         """
#         Draws a vertical line with a color.
        
#         Args:
#             x: The X coordinate of the line.
#             y0: The Y coordinate of the start (inclusive).
#             y1: The Y coordinate of the end (inclusive).
#             color: The color of the line.
#             alpha: The alpha value of the area (optional -- default 100%).
#                 Must be 0 <= alpha <= 1.
#         """
#         low = min(y0, y1)
#         high = max(y0, y1)
#         y = low
        
#         while y <= high:
#             self.point(x, y, color, alpha)
#             y += 1
        
            
# class GraphicsUtil:
#     def mix_colors(old_color: int, new_color: int, alpha: float) -> int:
#         """
#         Mixes two given colors together with an alpha value.
        
#         Args:
#             old_color: The color that was previously rendered behind the new color.
#             new_color: The new color to overlay on top of the old color.
#             alpha: A float between 0 and 1 defining the opacity of the new color.
            
#         Returns:
#             A new mixed RGB color.
#         """
#         if alpha < 0 or alpha > 1:
#             raise ValueError(f"Alpha value {alpha} is not bounded in 0 <= alpha <= 1.")
        
#         # Extract RGB components of each color
#         old_r = (old_color >> 16) & 0xFF
#         old_g = (old_color >> 8) & 0xFF
#         old_b = old_color & 0xFF

#         new_r = (new_color >> 16) & 0xFF
#         new_g = (new_color >> 8) & 0xFF
#         new_b = new_color & 0xFF

#         # Calculate the mixed RGB components
#         mixed_r = int(old_r * (1 - alpha) + new_r * alpha)
#         mixed_g = int(old_g * (1 - alpha) + new_g * alpha)
#         mixed_b = int(old_b * (1 - alpha) + new_b * alpha)

#         # Combine the RGB components back into a single integer
#         mixed_color = (mixed_r << 16) | (mixed_g << 8) | mixed_b

#         return mixed_color
    
#     def encode_color_565(color: int) -> int:
#         return ((color >> 8) & 0xF800) | ((color >> 5) & 0x07E0) | ((color >> 3) & 0x001F)