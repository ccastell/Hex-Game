
from src.views import Hex
from src.models.board import Board
from src.models.player import Player, Order


def start_game():

    board_model: Board = Board()
    player_1: Player = Player(Order.FIRST)
    player_2: Player = Player(Order.SECOND)

    game = Hex(board_model)
    game.on_execute(player_1, player_2)
