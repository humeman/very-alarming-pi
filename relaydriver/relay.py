import digitalio

class Relay:
    def __init__(self, pin):
        self._pin = digitalio.DigitalInOut(pin)
        self._pin.direction = digitalio.Direction.OUTPUT
        self._state = False
        self._pin.value = False
        
    def state(self) -> bool:
        return self._pin.value
    
    def on(self) -> bool:
        self._state = True
            
    def off(self) -> bool:
        self._pin.value = False
        