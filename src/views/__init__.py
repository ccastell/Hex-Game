import enum
import pygame

from typing import Union

from src.views.home_view import HomeView, HomeViewButton
from src.views.board_view import BoardView, BoardViewButton

from src.models.board import Board
from src.models.player import Player

from src.controllers.player_controller import PlayerController

class Screen(enum.Enum):
    HOME: int = 0
    BOARD: int = 1


class GameState(enum.Enum):
    TWO_PLAYER_GAME: int

#
# 
# Initializing Class Based Pygame
# http://pygametutorials.wikidot.com/tutorials-basic
#
class Hex:

    _current_screen: Screen = Screen.HOME 

    _home_view: HomeView
    _board_view: BoardView

    _board: Board

    def __init__(self, board: Board):
        self._running = True
        self._screen = None
        self._screen_size = self.width, self.height = 700, 700

        self._board = board


    def on_init(self, player_1: Player, player_2: Player):
        pygame.init()
        pygame.display.set_caption('Hex Game')
        
        self._screen = pygame.display.set_mode(
            self._screen_size, pygame.HWSURFACE | pygame.DOUBLEBUF
        )

        self._home_view = HomeView(self._screen, self._screen_size)
        self._board_view = BoardView(
            self._screen,
            self._screen_size,
            self._board,
            player_1,
            player_2
        )

        self._running = True

    def _on_mouse_down(self):
        mouse = pygame.mouse.get_pos()
        
        def _find_button() -> Union[HomeViewButton, BoardViewButton]:
            if self._current_screen == Screen.HOME:
                return self._home_view.on_mouse_down(mouse)
            elif self._current_screen == Screen.BOARD:
                return self._board_view.on_mouse_down(mouse)
            
        def _action(button: Union[HomeViewButton, BoardViewButton]) -> None:
            if button == HomeViewButton.TWO_PLAYER_GAME:
                self._board_view.start_2_player_game()
                self._current_screen = Screen.BOARD
            elif button == BoardViewButton.QUIT:
                self._current_screen = Screen.HOME

        _action(_find_button())

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            self._on_mouse_down()
 
    def on_loop(self):
        pass
 
    def on_render(self):
        if self._current_screen == Screen.HOME:
            self._home_view.update()
        elif self._current_screen == Screen.BOARD:
            self._board_view.update()
    
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self, player_1: Player, player_2: Player):
        if self.on_init(player_1, player_2) == False:
            self._running = False
 
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()
            
        self.on_cleanup()
 