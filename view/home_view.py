from pygame import Rect
from pygame.draw import rect
from pygame.font import Font
from pygame.display import update

from view.constant import MAIN_FONT, TITLE_FONT, LARGE_TEXT
from view.screen_view import ScreenView


class HomeView(ScreenView):

    def __init__(self, screen, size):
        super().__init__(screen, size)

        self._set_background()
        self._set_title()

        update()

    def _set_background(self):
        rect(
            self._screen,
            (246, 246, 246),
            Rect(
                0, 0, self._width, self._height
            )
        )

    def _set_title(self):
        title = Font(TITLE_FONT, LARGE_TEXT)
        textsurface = title.render(
            'Hex Game',
            False,
            (0, 0, 0)
        )
        titleRect = textsurface.get_rect()  
        titleRect.center =  (self._width // 2, self._height // 2)
        
        self._screen.blit(textsurface, titleRect)

    def _set_buttons(self):
        pass


    def update(self):
        pass