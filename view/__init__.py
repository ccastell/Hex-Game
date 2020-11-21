import enum
import pygame

from typing import Union

from view.home_view import HomeView, HomeViewButton
from view.board_view import BoardView, BoardViewButton



class Screen(enum.Enum):
    HOME: int = 0
    BOARD: int = 1

#
# 
# Initializing Class Based Pygame
# http://pygametutorials.wikidot.com/tutorials-basic
#
class Hex:

    _current_screen: Screen = Screen.HOME 

    _home_view: HomeView
    _board_view: BoardView

    def __init__(self):
        self._running = True
        self._screen = None
        self.size = self.width, self.height = 700, 700

    def on_init(self):
        pygame.init()
        pygame.display.set_caption('Hex Game')
        
        self._screen = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF
        )
 
        self._home_view = HomeView(self._screen, self.size)
        self._board_view = BoardView(self._screen, self.size)
        
        self._running = True

    def _on_mouse_button_down(self):
        mouse = pygame.mouse.get_pos()
        
        def _find_button() -> Union[HomeViewButton, BoardViewButton]:
            if self._current_screen == Screen.HOME:
                return self._home_view.mouse_button_down(mouse)
            elif self._current_screen == Screen.BOARD:
                return self._board_view.mouse_button_down(mouse)
            
        def _action(button: Union[HomeViewButton, BoardViewButton]) -> None:
            if button == HomeViewButton.TWO_PLAYER_GAME:
                self._current_screen = Screen.BOARD
            elif button == BoardViewButton.QUIT:
                self._current_screen = Screen.HOME
        
        _action(_find_button())

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            self._on_mouse_button_down()
 
    def on_loop(self):
        pass
 
    def on_render(self):
        if self._current_screen == Screen.HOME:
            self._home_view.update()
        elif self._current_screen == Screen.BOARD:
            self._board_view.update()
    
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()
            
        self.on_cleanup()
 