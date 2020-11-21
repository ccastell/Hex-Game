import enum 

from typing import Tuple, List


class State(enum.Enum):
    WHITE: int = 0
    RED: int = 0
    BLUE: int = 0

class Tile:

    __center: Tuple[int, int]

    __neighbors: List[Tuple[int, int]]

    __state: State = State.WHITE

    def __init__(self, center: Tuple[int, int], neighbors: List[Tuple[str, int]]):
        self.__center = center
        self.__neighbors = neighbors

    def center(self) -> Tuple[int, int]:
        return self.__center

    def neighbors(self) -> List[Tuple[str, int]]:
        return self.__neighbors

    def state(self) -> State:
        return self.__state

    def update_state(self, new_state) -> None:
        self.__state = new_state

    def __str__(self):
        return f'{self.__center[0]}{str(self.__center[1])}'