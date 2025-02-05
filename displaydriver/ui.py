from abc import ABC, abstractmethod
from typing import Any, List
import displayio

class UIElement(ABC):
    @abstractmethod
    def handle_click(self, x: int, y: int) -> bool:
        """
        Handles a button press. This UI element is responsible for:
        - Checking if the given coordinates are in this element's bounds
        - Running any actions
        - Returning True if future actions should be cancelled (if there's overlap)
        
        Args:
            x: X coordinate
            y: Y coordinate
            
        Returns:
            cancel: If True, handle_click will not be called on any other elements.
        """
        
    @abstractmethod
    def get_displayio_elements(self) -> List[Any]:
        """
        Returns all DisplayIO elements associated with this UI element.
        This list should not be modified during the lifecycle of the element.
        """
        
    @abstractmethod
    def tick(self) -> bool:
        """
        Runs many times per second. Use to do periodic updates.
        Return true to redraw.
        """