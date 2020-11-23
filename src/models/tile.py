from typing import Tuple, List

from src.models.constant import Color

class Tile:

    _id: Tuple[int, int]

    _neighbors: List[Tuple[int, int]]

    _color: Color = Color.WHITE

    _lock: bool

    def __init__(self, id: Tuple[int, int], neighbors: List[Tuple[str, int]]):
        self._id = id
        self._neighbors = neighbors
        self._color = Color.WHITE
        self._lock = False

    def id(self) -> Tuple[int, int]:
        return self._id

    def neighbors(self) -> List[Tuple[str, int]]:
        return self._neighbors

    def color(self) -> Color:
        return self._color

    def update_color(self, color) -> None:
        self._color = color

    def is_lock(self) -> bool:
        return self._lock

    def unlock_tile(self) -> None:
        self._lock = False

    def lock_tile(self) -> None:
        self._lock = True

    def __str__(self):
        return f'{self._id[0]}{str(self._id[1])}'