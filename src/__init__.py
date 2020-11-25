
from src.views import Hex
from src.models.board import Board
from src.models.player import Player, Order

from src.controllers.player_controller import PlayersController

def start_game():

    board_model: Board = Board()
    player_1: Player = Player(Order.FIRST)
    player_2: Player = Player(Order.SECOND)

    game = Hex(board_model, PlayersController(player_1, player_2))
    game.on_execute()
