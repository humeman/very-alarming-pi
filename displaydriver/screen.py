from abc import ABC, abstractmethod
from typing import Any, List
from displaydriver.ui import UIElement
import displayio

class Screen(ABC):
    @abstractmethod
    def tick(self) -> None:
        """
        Executes a tick. This method will be called many times per second.
        Any timed update tasks should be called here, like updating the value
        of the clock display.
        """
    
    @abstractmethod
    def handle_click(self, x: int, y: int) -> None:
        """
        Handles a click on the screen.
        
        Args:
            x: X coordinate of click.
            y: Y coordinate of click.
        """
        
    @abstractmethod
    def get_displayio_elements(self) -> List[Any]:
        """
        Returns a list of DisplayIO elements that can be added to
        and rendered on the root group of this screen. This list
        should not be updated during its lifetime.
        """
        
class UIScreen(Screen):
    def __init__(self):
        """
        Initializes an empty screen which can render UI elements.
        """
        self._ui_elements: List[UIElement] = []
        self._group = displayio.Group()
        
    def add_element(self, element: UIElement) -> None:
        """
        Adds a single element to the screen.
        
        Args:
            element: The element to add.
            
        Throws:
            ValueError: The element is already registered.
        """
        if element in self._ui_elements:
            raise ValueError("This element is already registered to this screen.")
        
        self._ui_elements.append(element)
        for dioelement in element.get_displayio_elements():
            self._group.append(dioelement)
        
    def remove_element(self, element: UIElement) -> None:
        """
        Removes a single element from the screen.
        
        Args:
            element: The element to remove.
            
        Throws:
            ValueError: The element isn't registered.
        """
        if element not in self._ui_elements:
            raise ValueError("This element is not registered to this screen.")
        
        self._ui_elements.remove(element)
        for dioelement in element.get_displayio_elements():
            self._group.remove(dioelement)
        
    def clear_elements(self) -> None:
        """
        Removes all elements from this screen.
        """
        self._ui_elements = []   
        self._group = displayio.Group()
        
    def handle_click(self, x, y):
        print(x, y)
        for element in self._ui_elements:
            element.handle_click(x, y)
    
    def tick(self) -> bool:
        draw = False
        for element in self._ui_elements:
            if element.tick():
                draw = True
        return draw
    
    def get_displayio_elements(self):
        return [self._group]