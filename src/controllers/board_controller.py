

from src.models.player import Player
from src.models.board import Board
from src.models.tile import Tile

from src.controllers.tile_controller import TileController

class BoardController:

    _board: Board

    def __init__(self, board: Board):
        self._board = board

    def append_history(self, tile: Tile):
        if self._board.is_current():
            self._board.append_history(tile)
        else:
            self._board.delete_last_move()
            self._board.append_history(tile)
        self._board.current()

    def undo_history(self, current_player: Player):
        number_moves: int = self._board.number_moves()
        if number_moves > 0 and self._board.is_current():
            last_tile: Tile = self._board.last_move()
            tile_controler = TileController(last_tile)

            if self._board.number_moves() == 1:
                if self._board.is_swapped():
                    tile_controler.update_color(current_player.color())
                    self._board.unswapped()
            if self._board.number_moves() >= 1:
                tile_controler.reset()
                self._board.not_current()

    def swap_first_tile(self, current_player: Player):

        if self._board.number_moves() == 1 and not self._board.is_swapped():
            first_tile: Tile = self._board.last_move()
            tile_controler = TileController(first_tile)
            tile_controler.update_color(current_player.color())
            self._board.swapped()

    def reset(self):
        self._board.initialize_matrix()
        self._board.initialize_history()
        self._board.unswapped()
        self._board.current()