import enum
from typing import Tuple, List

from pygame import Surface

from src.view.button_view import ButtonView

class ScreenView:
    
    _screen: Surface
    _width: float
    _height: float
    _center: Tuple[float, float]

    def __init__(self, screen: Surface, size: int):
        self._screen = screen   
        self._width, self._height = size
        self._center = (self._width // 2, self._height // 2)

    def update(self):
        raise NotImplementedError

    def _find_button(self, mouse: Tuple[int, int], buttons: List[ButtonView]) -> enum.Enum:
        for button in buttons:
            if button.collidepoint(mouse):
                return button.id()