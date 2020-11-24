
from src.models.player import Player, State


class PlayerController:

    _player: Player

    def __init__(self, player):
        self._player =  player

    def human(self):
        self._player.set_state(State.HUMAN)

    def computer(self):
        self._player.set_state(State.COMPUTER)

    def off(self):
        self._player.set_state(State.OFF)
