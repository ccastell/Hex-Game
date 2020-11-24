from enum import Enum

from src.models.constant import Color


class Order(Enum):
    FIRST: int = 0
    SECOND: int = 1

class State(Enum):
    OFF: int = 0
    HUMAN: int = 1
    COMPUTER: int = 2

class Player:
    
    _name: str
    _order: Order
    _color: Color

    _state: State

    def __init__(self, order: Order):
        self._order = order
        self._state = State.OFF

        if order == Order.FIRST:
            self._name = 'Player 1'
            self._color = Color.RED
        else:
            self._name = 'Player 2'
            self._color = Color.BLUE

    def name(self):
        return self._name

    def color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def state(self):
        self._state
    
    def set_state(self, state: State):
        self._state = state

    def order(self):
        return self._order
