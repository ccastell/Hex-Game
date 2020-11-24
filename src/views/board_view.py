import enum
from typing import Tuple, List, Optional, Dict, Any

from pygame import Rect, Surface
from pygame.draw import rect, polygon
from pygame.display import update
from pygame.font import Font

from src.views.screen_view import ScreenView
from src.views.button_view import ButtonView
from src.views.tile_view import TileView
from src.views.constant import WHITE, MAIN_BACKGROUND_COLOR, LARGE_PADDING, \
    BUTTON_BACKGROUND_COLOR, MAIN_FONT, MEDIUM_TEXT, RED_TILE, BLUE_TILE, BLACK, \
    LARGE_TEXT

from src.models.constant import Color
from src.models.board import Board
from src.models.player import Player

from src.controllers.board_controller import BoardController
from src.controllers.player_controller import PlayerController

PARALLELOGRAM = {
    'TOP': (
        (77, 129, 205),
        [
            (60, 133),
            (60 + 403, 133),
            (60 + 415, 153),
            (70, 153)
        ]
    )
    ,
    'BOTTOM': (
        (77, 129, 205),
        [
            (20 + 198, 145  + 330),
            (20 + 198 + 415, 145  + 330),
            (20 + 198 + 415, 145  + 330 + 20),
            (20 + 198 + 10, 145  + 330 + 20)
        ]
    ),
    'LEFT': (
        (218, 113, 123),
        [
            (30, 133) ,
            (60, 133),
            (60 + 198, 145 + 330),
            (20 + 198, 145  + 330)
        ]
    ),
    'RIGHT': (
        (218, 113, 123),
        [
            (20 + 415, 153),
            (60 + 415, 153),
            (50 + 198 + 415, 145 + 330 + 20),
            (20 + 198 + 415, 145  + 330 + 20)
        ]
    )
}


class BoardViewButton(enum.Enum):
    QUIT: int = 0,
    UNDO: int = 1,
    SWAP: int = 2
    HINT: int = 3
    TILE: int = 4


class BoardView(ScreenView):

    _buttons: List[ButtonView]
    _tiles: List[TileView]

    _board: Board

    _player_1: Player
    _player_2: Player

    _player_1_controller: PlayerController
    _player_2_controller: PlayerController

    _current_player: Player

    def __init__(self,
                 screen: Surface,
                 size: int,
                 board: Board,
                 player_1: Player,
                 player_2: Player):
        super().__init__(screen, size)
        
        self._board = board
        
        self._board_controller = BoardController(board)

        self._player_1 = player_1
        self._player_2 = player_2 

        self._player_1_controller = PlayerController(player_1)
        self._player_2_controller = PlayerController(player_2)

        self._current_player = player_1

    def start_2_player_game(self):
        self._player_1_controller.human()
        self._player_2_controller.human()

    def _draw_background(self):
        rect(
            self._screen,
            MAIN_BACKGROUND_COLOR,
            Rect(
                0, 0, self._width, self._height
            )
        )

    def _button_views(self):
        return [
            {'ID': BoardViewButton.QUIT, 'TEXT': 'Quit', 'LOCATION':  (self._width - (65.5 + 50 - 27), self._height - 50), 'BACKGROUND': BUTTON_BACKGROUND_COLOR},
            {'ID': BoardViewButton.SWAP, 'TEXT': 'Swap', 'LOCATION': (self._width - 355 - 5, self._height - 50), 'BACKGROUND': (153, 153, 255)},
            {'ID': BoardViewButton.UNDO, 'TEXT': 'Undo', 'LOCATION': (self._width - 318.5 + 55, self._height - 50), 'BACKGROUND': (153, 153, 255)},
            {'ID': BoardViewButton.HINT, 'TEXT': 'Hint', 'LOCATION': (self._width - 228.5 + 55, self._height - 50), 'BACKGROUND': (204, 153, 255)}
        ]


    def _draw_buttons(self):
        def _draw_button(button: Dict[str, Any]):
            disabled = False

            if button['ID'] == BoardViewButton.SWAP:
                disabled = self._board.move_count() != 1 or self._board.is_swapped() or self._board.game_over()
            elif button['ID'] == BoardViewButton.UNDO:
                disabled = self._board.move_count() < 1 or not self._board.is_current() or self._board.game_over()

            return ButtonView(
                button['ID'],
                self._screen,
                button['LOCATION'],
                button['TEXT'],
                text_color=WHITE,
                background_color=button['BACKGROUND'],
                disabled = disabled
            )

        self._buttons = [
            _draw_button(button)
            for button in self._button_views()
        ]

    def _draw_parallelogram(self):
        for color, shape in PARALLELOGRAM.values():
            polygon(
                self._screen,
                color,
                shape           
            )            

    def _draw_tile(self, x_index, y_index):
        x_coord = 90 + (17 * y_index) + (35 * x_index)
        y_coord = 165 + (30 * y_index) 
        return TileView(
            self._screen,
            self._board.find_tile(x_index, y_index),
            (x_coord, y_coord)
        )

    def _draw_tiles(self):

        self._draw_parallelogram()

        self._tiles = [
            [
                self._draw_tile(x_index, y_index)
                for x_index in range(0, self._board.size())
            ]
            for y_index in range(0, self._board.size())     
        ]

    def _draw_winning_labels(self):
        label: Font = Font(MAIN_FONT, MEDIUM_TEXT)
        label_surface: Surface = label.render(
            'Game Over!!',
            True,
            BLACK
        )
        label_rect: Rect = label_surface.get_rect()
        label_rect.center = (87 + 50, self._height - 50)
        self._screen.blit(label_surface, label_rect)

        player_label: Font = Font(MAIN_FONT, LARGE_TEXT)
        player_label_surface: Surface = player_label.render(
            f'{self._current_player.name()} Wins!!',
            True,
            RED_TILE if self._current_player.color() == Color.RED else BLUE_TILE
        )
        player_label_rect: Rect = player_label_surface.get_rect()
        player_label_rect.center = (self._width / 2, self._height - 150)
        self._screen.blit(player_label_surface, player_label_rect)

    def _draw_labels(self):

        if self._board.game_over():
            self._draw_winning_labels()
        else:
            label: Font = Font(MAIN_FONT, MEDIUM_TEXT)
            label_surface: Surface = label.render(
                'Turn: ',
                True,
                BLACK
            )
            label_rect: Rect = label_surface.get_rect()
            label_rect.center = (36 + 50, self._height - 50)
            self._screen.blit(label_surface, label_rect)

            player_label: Font = Font(MAIN_FONT, MEDIUM_TEXT)
            player_label_surface: Surface = player_label.render(
                self._current_player.name(),
                True,
                RED_TILE if self._current_player.color() == Color.RED else BLUE_TILE
            )
            plauer_label_rect: Rect = player_label_surface.get_rect()
            plauer_label_rect.center = (56 + 50 + 80, self._height - 50)

            self._screen.blit(player_label_surface, plauer_label_rect)


    def _tile_clicked(self, mouse: Tuple[int, int]) -> bool:
        for row in self._tiles:
            for tile_view in row:
                if tile_view.collidepoint(mouse) and tile_view.on_mouse_down(self._current_player):
                    self._board_controller.set_last_move(tile_view.tile())
                    return True
        return False
    
    def _swap_first_tile(self):
        self._board_controller.swap_first_tile(self._current_player)

    def _change_current_player(self):
        if self._current_player == self._player_1:
            self._current_player = self._player_2
        else:
            self._current_player = self._player_1
    
    def on_mouse_down(self, mouse: Tuple[int, int]) -> enum.Enum:
        button_clicked = self._find_button(
            mouse,
            self._buttons
        )
        
        if button_clicked == BoardViewButton.QUIT:
            self._board_controller.reset()
            return button_clicked
        elif button_clicked == BoardViewButton.SWAP:
            self._swap_first_tile()
            self._change_current_player()
        elif button_clicked == BoardViewButton.UNDO:
            self._board_controller.undo(self._current_player)
            self._change_current_player()
        elif button_clicked == BoardViewButton.HINT:
            print("Hint Clicked")
        else:
            if self._tile_clicked(mouse):
                self._board_controller.check_win()
                if not self._board.game_over():
                    self._change_current_player()
            else:
                print("Not Registered")       

    def update(self):
        self._draw_background()
        self._draw_buttons()
        self._draw_tiles()
        self._draw_labels()
        update()
