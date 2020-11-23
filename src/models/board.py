from typing import Tuple, List

from src.models.tile import Tile
from src.models.constant import Color

class Board:

    _size: int

    _matrix: Tuple[Tuple[Tile , ...], ...]

    _is_swapped: bool = False
    
    _is_current: bool = True
    _history: List[Tile] = []


    def __init__(self):
        self._size = 11

        self.initialize_matrix()
        self.initialize_history()


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
                            lambda neighbor: False if neighbor[0] < 0 or neighbor[1] < 0 else True,
                            _neighbors(column_index, row_index)
                        ))
                    )
                )
            self._matrix.append(row)

    def initialize_history(self):
        self._history = []


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

    def number_moves(self) -> int:
        return len(self._history)

    def last_move(self):
        return self._history[-1]

    def delete_last_move(self):
        self._history = self._history[:-1]

    def append_history(self, tile: Tile):
        self._history.append(tile)

    def check_win(self):
        # TODO: Check the win condition
        raise NotImplementedError
