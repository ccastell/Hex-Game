import enum
from typing import Tuple, List

from pygame import Rect, Surface
from pygame.draw import rect
from pygame.font import Font
from pygame.display import update

from view.screen_view import ScreenView
from view.button_view import ButtonView
from view.constant import (
    MAIN_FONT, TITLE_FONT, LARGE_TEXT, MEDIUM_TEXT,
    MAIN_BACKGROUND_COLOR, MAIN_TEXT_COLOR, SUB_TEXT_COLOR,
    MEDIUM_PADDING, LARGE_PADDING, BUTTON_BACKGROUND_COLOR, WHITE)
    
class HomeViewButton(enum.Enum):
    TWO_PLAYER_GAME: int = 0,

class HomeView(ScreenView):

    _two_player_button: ButtonView

    def __init__(self, screen: Surface, size: int):
        super().__init__(screen, size)

    def _draw_background(self):
        rect(
            self._screen,
            MAIN_BACKGROUND_COLOR,
            Rect(
                0, 0, self._width, self._height
            )
        )

    def _draw_title(self):
        subtitle: Font = Font(MAIN_FONT, MEDIUM_TEXT)
        subtitle_surface: Surface = subtitle.render(
            'Carl&Co. Games',
            True,
            SUB_TEXT_COLOR
        )
        subtitle_rect: Rect = subtitle_surface.get_rect()  


        title: Font = Font(TITLE_FONT, LARGE_TEXT)
        title_surface: Surface = title.render(
            'The Hex Game',
            True,
            MAIN_TEXT_COLOR
        )
        title_rect: Rect = title_surface.get_rect()  

        title_rect.center = (
            self._center[0],
            self._center[1] - 50
        )       
        height_offset: int = (title_rect.height // 2) + MEDIUM_PADDING

        subtitle_rect.center =  (
            title_rect.center[0],
            title_rect.center[1] - height_offset
        )

        self._screen.blit(title_surface, title_rect)
        self._screen.blit(subtitle_surface, subtitle_rect)

    def _draw_buttons(self):
        self._two_player_button = ButtonView(
            HomeViewButton.TWO_PLAYER_GAME,
            self._screen,
            (self._center[0], self._center[1] + (LARGE_PADDING * 3)),
            '2-Player Game',
            text_color=WHITE,
            background_color=BUTTON_BACKGROUND_COLOR
        )

    def mouse_button_down(self, mouse: Tuple[int, int]) -> enum.Enum:
        return self._find_button(mouse, [self._two_player_button])

    def update(self):
        self._draw_background()
        self._draw_title()
        self._draw_buttons()
        update()
