
from src.views import Hex
from src.models.board import Board

def start_game():

    board_model: Board = Board()

    game = Hex(board_model)
    game.on_execute()
