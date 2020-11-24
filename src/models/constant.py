from enum import Enum

class Color(Enum):
    WHITE: int = 0
    RED: int = 1
    BLUE: int = 2

class HeuristicDirection(Enum):
    TOP: int = 0
    BOTTOM: int = 1
    LEFT: int = 3
    RIGHT: int = 4