from src.models.tile import Tile

class TileController:
    
    _tile: Tile

    def __init__(self, tile: Tile):
        self._tile = tile

    