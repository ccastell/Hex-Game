import enum
import pygame

from view.home_view import HomeView
from view.board_view import BoardView



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

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
 
    def on_loop(self):
        pass
 
    def on_render(self):
        if self._screen == Screen.HOME:
            self._home_view.update()
        elif self._screen == Screen.BOARD:
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
 