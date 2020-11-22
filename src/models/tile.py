import enum 

from typing import Tuple, List


class State(enum.Enum):
    WHITE: int = 0
    RED: int = 1
    BLUE: int = 2

class Tile:

    _id: Tuple[int, int]

    _neighbors: List[Tuple[int, int]]

    _state: State = State.WHITE

    def __init__(self, id: Tuple[int, int], neighbors: List[Tuple[str, int]]):
        self._id = id
        self._neighbors = neighbors
        self._state = State.BLUE

    def id(self) -> Tuple[int, int]:
        return self._id

    def neighbors(self) -> List[Tuple[str, int]]:
        return self._neighbors

    def state(self) -> State:
        return self._state

    def update_state(self, new_state) -> None:
        self.__state = new_state

    def __str__(self):
        return f'{self._id[0]}{str(self._id[1])}'