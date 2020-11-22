from typing import Tuple

from src.models.tile import Tile

class Board:

    _size: int

    _matrix: Tuple[Tuple[Tile , ...], ...] = []

    def __init__(self):
        self._size = 11

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

    def matrix(self) -> Tuple[Tuple[Tile , ...], ...]:
        return self._matrix

    def size(self) -> int:
        return self._size

    def find_tile(self, x, y) -> Tile:
        return self._matrix[y][x]

    def check_win(self):
        # TODO: Check the win condition
        raise NotImplementedError
