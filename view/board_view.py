import enum
from typing import Tuple

from pygame import Rect, Surface
from pygame.draw import rect
from pygame.display import update

from view.screen_view import ScreenView
from view.button_view import ButtonView
from view.constant import WHITE, MAIN_BACKGROUND_COLOR, LARGE_PADDING, BUTTON_BACKGROUND_COLOR

class BoardViewButton(enum.Enum):
    QUIT: int = 0,
    UNDO: int = 1,
    REDO: int = 2
    HINT: int = 3

class BoardView(ScreenView):
    
    _quit_button: ButtonView
    _undo_button: ButtonView
    _redo_button: ButtonView 
    _hint_button: ButtonView 


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

    def _draw_buttons(self):

        self._quit_button = ButtonView(
            BoardViewButton.QUIT,
            self._screen,
            (self._width - (65.5 + 50), self._height - 50),
            'Quit Game',
            text_color=WHITE,
            background_color=BUTTON_BACKGROUND_COLOR
        )
        # 131

        # (65.5 + 50 + 65.5 + 37.5 + 10 + 80 + 10 + 84 + 10)
        self._undo_button = ButtonView(
            BoardViewButton.UNDO,
            self._screen,
            (self._width - 412.5, self._height - 50),
            'Undo',
            text_color=WHITE,
            background_color=(153, 153, 255)
        )

        # (65.5 + 50 + 65.5 + 37.5 + 10 + 80 + 10)
        self._redo_button = ButtonView(
            BoardViewButton.REDO,
            self._screen,
            (self._width - 318.5, self._height - 50),
            'Redo',
            text_color=WHITE,
            background_color=(153, 153, 255)
        )
        # 81

        # (65.5 + 50 + 65.5 + 37.5 + 10)
        self._hint_button = ButtonView(
            BoardViewButton.HINT,
            self._screen,
            (self._width - 228.5, self._height - 50),
            'Hint',
            text_color=WHITE,
            background_color=(204, 153, 255)
        )
        # 75

    def mouse_button_down(self, mouse: Tuple[int, int]) -> enum.Enum:
        button_clicked = self._find_button(
            mouse,
            [self._quit_button, self._hint_button, self._redo_button, self._undo_button]
        )
        
        if button_clicked == BoardViewButton.QUIT:
            return button_clicked
        elif button_clicked == BoardViewButton.REDO:
            print("Redo Clicked")
        elif button_clicked == BoardViewButton.UNDO:
            print("Undo Clicked")
        elif button_clicked == BoardViewButton.HINT:
            print("Hint Clicked")
        else:
            print("Not Registered")
        

    def update(self):
        self._draw_background()
        self._draw_buttons()
        update()
