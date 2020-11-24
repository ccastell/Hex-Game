from typing import Tuple, List

from src.models.tile import Tile
from src.models.constant import Color, HeuristicDirection


class Board:

    _size: int

    _matrix: Tuple[Tuple[Tile , ...], ...]

    _is_swapped: bool = False
    _is_current: bool = True

    _move_count: int = 0
    _last_move: Tile

    _game_over: bool = False

    def __init__(self):
        self._size = 11

        self.initialize_matrix()

    def initialize_matrix(self):
        self._matrix = []

        def _neighbors(column_index, row_index):
            return [
                (column_index, row_index - 1), (column_index + 1, row_index - 1),
                (column_index - 1, row_index), (column_index + 1, row_index), 
                (column_index - 1, row_index + 1), (column_index, row_index + 1)
            ]

        for row_index in range(0, self._size):
            row = []
            for column_index in range(0, self._size):
                row.append(
                    Tile(
                        (column_index, row_index),
                        list(filter(
                            lambda neighbor: True if 0 <= neighbor[0] <= 10 and 0 <= neighbor[1] <= 10 else False,
                            _neighbors(column_index, row_index)
                        ))
                    )
                )
            self._matrix.append(row)

    def matrix(self) -> Tuple[Tuple[Tile , ...], ...]:
        return self._matrix

    def size(self) -> int:
        return self._size

    def find_tile(self, x, y) -> Tile:
        return self._matrix[y][x]

    def is_swapped(self) -> bool:
        return self._is_swapped

    def swapped(self):
        self._is_swapped = True
    
    def unswapped(self):
        self._is_swapped = False

    def is_current(self):
        return self._is_current

    def current(self):
        self._is_current = True

    def not_current(self):
        self._is_current = False

    def last_move(self):
        return self._last_move

    def set_last_move(self, tile):
        self._last_move = tile

    def move_count(self) -> int:
        return self._move_count

    def decrement_move_count(self):
        self._move_count -= 1

    def increment_move_count(self):
        self._move_count += 1

    def append_history(self, tile: Tile):
        self._last_move = tile
        self._move_count += 1

    def set_game_over(self):
        self._game_over = True
    
    def game_over(self):
        return self._game_over

    def reset(self):
        self._game_over = False
        self.initialize_matrix()
        self._move_count = 0
        self._last_move = None
        self.unswapped()
        self.current()