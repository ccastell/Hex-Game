from typing import Tuple

from tile import Tile

class Board:

    __size: int

    __matrix: Tuple[Tuple[Tile , ...], ...] = []

    def __init__(self, size):
        self.__size = size


        def __neighbors(column_index, row_index):
            return [
                (column_index, row_index - 1), (column_index + 1, row_index - 1),
                (column_index - 1, row_index), (column_index + 1, row_index), 
                (column_index - 1, row_index + 1), (column_index, row_index + 1)
            ]

        for row_index in range(0, self.__size):
            column = []
            for column_index in range(0, self.__size):
                column.append(
                    Tile(
                        (column_index, row_index - 1),
                        list(filter(
                            lambda neighbor: False if neighbor[0] < 0 or neighbor[1] < 0 else True,
                            __neighbors(column_index, row_index)
                        ))
                    )
                )

    def matrix(self):
        return self.__matrix

    def check_win(self):
        # TODO: Check the win condition
        raise NotImplementedError

if __name__ == "__main__":
    board = Board(11)
    print(board.matrix())