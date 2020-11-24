
from src.models.constant import Color
from src.models.tile import Tile
from src.models.player import Player, Order


class TileController:
    
    _tile: Tile

    def __init__(self, tile: Tile):
        self._tile = tile

    def on_player_clicked(self, player: Player) -> bool:
        if not self._tile.is_lock():
            self._tile.update_color(player.color())
            self._tile.lock_tile()
            return True
        return False

    def reset(self):
        self._tile.update_color(Color.WHITE)
        self._tile.unlock_tile()

    def update_color(self, color: Color):
        self._tile.update_color(color)

    def lock(self):
        self._tile.lock_tile()
