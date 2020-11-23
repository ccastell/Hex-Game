import enum 

from typing import Tuple, Dict

from pygame import Rect, Surface
from pygame.image import load
from pygame.draw import rect

from src.models.constant import Color as TileColor
from src.models.tile import Tile
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

    _hexagon: Surface
    _hexagon_rect: Rect

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

        tile_color = self._tile.color()

        def _image_source():
            if tile_color == TileColor.BLUE:
                return f'{self._tile_hexagon_location}/blue.png'
            elif tile_color == TileColor.RED:
                return f'{self._tile_hexagon_location}/red.png'
            else:
                return f'{self._tile_hexagon_location}/white.png'

        return load(_image_source())

    def _draw_tile(self):
        self._hexagon = self._hexagon_image()
        
        self._hexagon_rect: Rect = self._hexagon.get_rect()
        self._hexagon_rect.center = self._center
        self._screen.blit(
            self._hexagon,
            self._hexagon_rect
        )

    def tile(self):
        return self._tile

    def on_mouse_down(self, player):
        return self._tile_controler.on_player_clicked(player)
    
    def collidepoint(self, mouse: Tuple[int, int]):
        return self._hexagon_rect.collidepoint(mouse)

    