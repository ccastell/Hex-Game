
from src.models.constant import Color
from src.models.tile import Tile
from src.models.player import Player, Order


class TileController:
    
    _tile: Tile

    def __init__(self, tile: Tile):
        self._tile = tile

    def on_player_clicked(self, player: Player) -> bool:
        if not self._tile.is_lock():
            self._tile.set_color(player.color())
            self._tile.lock()

    def reset(self):
        self._tile.set_color(Color.WHITE)
        self._tile.unlock()

    def set_color(self, color: Color):
        self._tile.set_color(color)

    def lock(self):
        self._tile.lock()
