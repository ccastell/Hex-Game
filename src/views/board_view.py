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
    LARGE_TEXT, MAIN_TEXT_COLOR, TITLE_FONT, SUB_TEXT_COLOR

from src.models.constant import Color
from src.models.board import Board
from src.models.player import Player

from src.controllers.board_controller import BoardController
from src.controllers.player_controller import PlayersController

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


class BoardButtonsViews:

    _screen: Surface
    _buttons: Dict[str, Any]

    def __init__(self, screen: Surface, width: int, height: int):
        self._screen = screen

        self._buttons = [
            {'ID': BoardViewButton.QUIT, 'TEXT': 'Quit', 'LOCATION':  (width - (65.5 + 50 - 27), height - 50), 'BACKGROUND': BUTTON_BACKGROUND_COLOR},
            {'ID': BoardViewButton.SWAP, 'TEXT': 'Swap', 'LOCATION': (width - 355 - 5, height - 50), 'BACKGROUND': (153, 153, 255)},
            {'ID': BoardViewButton.UNDO, 'TEXT': 'Undo', 'LOCATION': (width - 318.5 + 55, height - 50), 'BACKGROUND': (153, 153, 255)},
            {'ID': BoardViewButton.HINT, 'TEXT': 'Hint', 'LOCATION': (width - 228.5 + 55, height - 50), 'BACKGROUND': (204, 153, 255)}
        ]

    def _draw_button(self,
                     button,
                     move_count: int,
                     is_swapped: bool,
                     is_current: bool,
                     game_over: bool):
        
        disabled = False

        if button['ID'] == BoardViewButton.SWAP:
            disabled = move_count != 1 or is_swapped or game_over
        elif button['ID'] == BoardViewButton.UNDO:
            disabled = move_count < 1 or not is_current or game_over
        elif button['ID'] == BoardViewButton.HINT:
            disabled = game_over
             

        return ButtonView(
            button['ID'],
            self._screen,
            button['LOCATION'],
            button['TEXT'],
            text_color=WHITE,
            background_color=button['BACKGROUND'],
            disabled = disabled
        )

    def draw(self,
             move_count: int,
             is_swapped: bool,
             is_current: bool,
             game_over: bool) -> List[ButtonView]:
        return [
            self._draw_button(button, move_count, is_swapped, is_current, game_over)
            for button in self._buttons
        ]

class BoardLabelViews:

    _screen: Surface

    _width: int
    _height: int

    def __init__(self, screen: Surface, width: int, height: int):
        self._screen = screen
        self._width = width
        self._height = height

    def _draw_title(self):
        label: Font = Font(TITLE_FONT, LARGE_TEXT)
        label_surface: Surface = label.render(
            'The Hex Game',
            True,
            SUB_TEXT_COLOR
        )
        label_rect: Rect = label_surface.get_rect()
        label_rect.center = (self._width / 2, (label_rect.height / 2))
        self._screen.blit(label_surface, label_rect)

    def _draw_winning_labels(self, current_player: Player):
        label: Font = Font(TITLE_FONT, MEDIUM_TEXT)
        label_surface: Surface = label.render(
            'Game Over!!',
            True,
            BLACK
        )
        label_rect: Rect = label_surface.get_rect()
        label_rect.center = (87 + 50, self._height - 50)
        self._screen.blit(label_surface, label_rect)

        player_label: Font = Font(TITLE_FONT, LARGE_TEXT)
        player_label_surface: Surface = player_label.render(
            f'{current_player.name()} Wins!!',
            True,
            RED_TILE if current_player.color() == Color.RED else BLUE_TILE
        )
        player_label_rect: Rect = player_label_surface.get_rect()
        player_label_rect.center = (self._width / 2, self._height - 150)
        self._screen.blit(player_label_surface, player_label_rect)

    def _draw_game_labels(self, current_player: Player):
        label: Font = Font(MAIN_FONT, MEDIUM_TEXT)
        label_surface: Surface = label.render(
            'Turn: ',
            True,
            BLACK
        )
        label_rect: Rect = label_surface.get_rect()
        label_rect.center = ((label_rect.width / 2) + 50, self._height - 50)
        self._screen.blit(label_surface, label_rect)

        player_label: Font = Font(TITLE_FONT, MEDIUM_TEXT)
        player_label_surface: Surface = player_label.render(
            current_player.name(),
            True,
            RED_TILE if current_player.color() == Color.RED else BLUE_TILE
        )
        plauer_label_rect: Rect = player_label_surface.get_rect()
        plauer_label_rect.center = (
            (plauer_label_rect.width / 2) + 50 + label_rect.width,
            self._height - 50
        )

        self._screen.blit(player_label_surface, plauer_label_rect)

    def draw(self, current_player, game_over: bool):
        self._draw_title()

        if game_over:
            self._draw_winning_labels(current_player)
        else:
            self._draw_game_labels(current_player)


class BoardView(ScreenView):

    _buttons: List[ButtonView]
    _tiles: List[TileView]

    _board: Board

    _players_controller: PlayersController

    _current_player: Player

    _button_views: BoardButtonsViews
    _label_views: BoardLabelViews

    def __init__(self,
                 screen: Surface,
                 size: int,
                 board: Board,
                 players_controller: PlayersController):
        super().__init__(screen, size)
        
        self._board = board
        
        self._board_controller = BoardController(board)

        self._players_controller = players_controller

        self._button_views = BoardButtonsViews(screen, self._width, self._height)
        self._label_views = BoardLabelViews(screen, self._width, self._height)

    def start_2_player_game(self):
        self._players_controller.two_player_game()

    def _draw_background(self):
        rect(
            self._screen,
            MAIN_BACKGROUND_COLOR,
            Rect(
                0, 0, self._width, self._height
            )
        )

    def _draw_buttons(self):
        self._buttons = self._button_views.draw(
            self._board.move_count(),
            self._board.is_swapped(),
            self._board.is_current(),
            self._board.game_over()
        )

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

    def _draw_labels(self):
        self._label_views.draw(self._players_controller.current_player(), self._board.game_over())

    def _on_tile_clicked(self, mouse: Tuple[int, int]) -> bool:
        for row in self._tiles:
            for tile_view in row:
                if tile_view.collidepoint(mouse) and tile_view.on_mouse_down(self._players_controller.current_player()):
                    self._board_controller.set_last_move(tile_view.tile())
                    return True
        return False
    
    def _on_swap_first_tile(self):
        self._board_controller.swap_first_tile(self._players_controller.current_player())
    
    def on_mouse_down(self, mouse: Tuple[int, int]) -> enum.Enum:
        button_clicked = self._find_button(
            mouse,
            self._buttons
        )
        
        if button_clicked == BoardViewButton.QUIT:
            self._board_controller.reset()
            self._players_controller.reset()
            return button_clicked
        elif button_clicked == BoardViewButton.SWAP:
            self._on_swap_first_tile()
            self._players_controller.change_current_player()
        elif button_clicked == BoardViewButton.UNDO:
            self._board_controller.undo(self._players_controller.current_player())
            self._players_controller.change_current_player()
        elif button_clicked == BoardViewButton.HINT:
            self._board_controller.hint(self._players_controller.current_player())
            self._board_controller.check_win()
            if not self._board.game_over():
                self._players_controller.change_current_player()
        else:
            if self._on_tile_clicked(mouse):
                self._board_controller.check_win()
                if not self._board.game_over():
                    self._players_controller.change_current_player()
            else:
                print("Not Registered")       

    def update(self):
        self._draw_background()
        self._draw_buttons()
        self._draw_tiles()
        self._draw_labels()
        update()
