from typing import Tuple, List, Dict

from src.models.constant import Color, HeuristicDirection

class Tile:

    _id: Tuple[int, int]

    _neighbors: List[Tuple[int, int]]

    _color: Color = Color.WHITE

    _lock: bool

    _heuristics: Dict[HeuristicDirection, int]

    def __init__(self, id: Tuple[int, int], neighbors: List[Tuple[str, int]]):
        self._id = id
        self._neighbors = neighbors
        self._color = Color.WHITE
        self._lock = False

        x_coordinate, y_coordinate = id
        self._heuristics = {
            Color.BLUE: {
                HeuristicDirection.TOP: y_coordinate,
                HeuristicDirection.BOTTOM: 10 - y_coordinate,
            },
            Color.RED: {
                HeuristicDirection.LEFT: x_coordinate,
                HeuristicDirection.RIGHT: 10 - x_coordinate
            }
        }

    def id(self) -> Tuple[int, int]:
        return self._id

    def neighbors(self) -> List[Tuple[str, int]]:
        return self._neighbors

    def color(self) -> Color:
        return self._color

    def update_color(self, color: Color) -> None:
        self._color = color

    def is_lock(self) -> bool:
        return self._lock

    def unlock_tile(self) -> None:
        self._lock = False

    def lock_tile(self) -> None:
        self._lock = True

    def heuristics(self) -> Dict[HeuristicDirection, int]:
        return self._heuristics[self._color]

    def __str__(self):
        return f'{self._id[0]}{str(self._id[1])}'
