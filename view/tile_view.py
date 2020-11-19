import enum 

from typing import Tuple, Dict


class Point(enum.Enum):
    TOP_RIGHT: int = 1
    MID_RIGHT: int = 2
    BOTTOM_RIGHT: int = 3
    BOTTOM_LEFT: int = 4
    MID_LEFT: int = 5
    TOP_LEFT: int = 6


class TileView:

    __center: Tuple[float, float] = (0, 0)

    __top_right: Tuple[float, float] = (0, 0)
    __mid_right: Tuple[float, float] = (0, 0)
    __bottom_right: Tuple[float, float] = (0, 0)
    __bottom_left: Tuple[float, float] = (0, 0)
    __mid_left: Tuple[float, float] = (0, 0)
    __top_left: Tuple[float, float] = (0, 0)

    def __init__(self, center: Tuple[float, float]):
        self.__center = center

    def center(self) -> Tuple[float, float]:
        return self.__center

    def corners(self) -> Dict[str: Tuple[float, float]]:
        return {
            Point.TOP_RIGHT: self.__top_right,
            Point.MID_RIGHT: self.__mid_right,
            Point.BOTTOM_RIGHT: self.__bottom_right,
            Point.BOTTOM_LEFT: self.__bottom_left,
            Point.MID_LEFT: self.__mid_left,
            Point.TOP_LEFT: self.__top_left
        }