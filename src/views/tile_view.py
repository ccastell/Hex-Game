import enum 

from typing import Tuple, Dict

from pygame import Rect, Surface
from pygame.image import load
from pygame.draw import rect

from src.models.tile import Tile, State as TileState
from src.controllers.tile_controller import TileController

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

    _tile: Tile
    _tile_controler: TileController

    _tile_container: Rect

    _tile_hexagon_location: str = 'resources/images/hexagon'

    def __init__(self,
                 screen: Surface,
                 tile: Tile,
                 center: Tuple[float, float]):

        self._screen = screen
        self._center = center

        self._tile = tile
        self._tile_controler = TileController(tile)

        self._draw_tile()

    def _hexagon_image(self):

        tile_state = self._tile.state()

        def _image_source():
            if tile_state == TileState.BLUE:
                return f'{self._tile_hexagon_location}/blue.png'
            elif tile_state == TileState.RED:
                return f'{self._tile_hexagon_location}/red.png'
            else:
                return f'{self._tile_hexagon_location}/white.png'

        return load(_image_source())

    def _draw_tile(self):
        hexagon_image = self._hexagon_image()
        
        image_rect: Rect = hexagon_image.get_rect()
        image_rect.center = self._center
        self._screen.blit(
            hexagon_image,
            image_rect
        )
