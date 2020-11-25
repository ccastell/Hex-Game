from src.models.player import Player, State


class PlayersController:

    _player_1: Player
    _player_2: Player

    _current_player: Player

    def __init__(self, player_1: Player, player_2: Player):
        self._player_1 = player_1
        self._player_2 = player_2

        self._current_player = player_1

    def current_player(self) -> Player:
        return self._current_player 

    def two_player_game(self):
        self._player_1.set_state(State.HUMAN)
        self._player_2.set_state(State.HUMAN)


    def change_current_player(self):
        if self._current_player == self._player_1:
            self._current_player = self._player_2
        else:
            self._current_player = self._player_1

    def reset(self):
        self._current_player = self._player_1