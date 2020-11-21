import enum 

from typing import Tuple, Dict

from pygame import Rect, Surface
from pygame.draw import rect


class Point(enum.Enum):
    TOP_RIGHT: int = 1
    MID_RIGHT: int = 2
    BOTTOM_RIGHT: int = 3
    BOTTOM_LEFT: int = 4
    MID_LEFT: int = 5
    TOP_LEFT: int = 6


class TileView:

    _screen: Surface
    _center: Tuple[float, float]

    _tile_container: Rect

    def __init__(self,
                 screen: Surface,
                 center: Tuple[float, float],
                 size: int = 10):
        self._screen = screen
        self._center = center


        self._draw_tile()

    def _draw_tile(self):
        self._tile_container = rect(
            self._screen,
            self._background_color
        )