from typing import Tuple, Any, Optional

from pygame.mouse import get_pos
from pygame import Rect, Surface
from pygame.font import Font
from pygame.draw import rect

from view.constant import (
    MAIN_FONT, SMALL_PADDING, MEDIUM_PADDING, SMALL_TEXT,
    BLACK, WHITE
)

class ButtonView:

    _screen: Surface
    _center: Tuple[float, float]
    _text: str
    _background_color: Tuple[int, int, int]

    _text_rect: Rect
    _text_surface: Surface

    _button_contianer: Rect

    def __init__(self,
                 id: Any,
                 screen: Surface,
                 center: Tuple[float, float],
                 text: str,
                 text_color: Tuple[int, int, int] = BLACK,
                 background_color: Tuple[int, int, int] = WHITE):

        self._id = id

        self._screen = screen
        self._center = center

        self._text = text 
        self._background_color = background_color
        self._text_color = text_color

        self._draw_text()
        self._draw_button()
    
        self._screen.blit(self._text_surface, self._text_rect) 



    def _draw_text(self):
        text = Font(MAIN_FONT, SMALL_TEXT)
        self._text_surface = text.render(
            self._text,
            True,
            self._text_color
        )

        self._text_rect = self._text_surface.get_rect() 
        self._text_rect.center = self._center


    def _draw_button(self):
        self._button_contianer = rect(
            self._screen,
            self._background_color,
            Rect(
                self._text_rect.x - (MEDIUM_PADDING * 2),
                self._text_rect.y - SMALL_PADDING,
                self._text_rect.width + (MEDIUM_PADDING * 4),
                self._text_rect.height + (SMALL_PADDING * 2)
            ),
            border_radius = 8
        )

    def id(self):
        return self._id

    def collidepoint(self, mouse: Tuple[int, int]):
        return self._text_rect.collidepoint(mouse) or self._button_contianer.collidepoint(mouse)
