from typing import List, Tuple

from random import choice

from src.models.player import Player
from src.models.board import Board
from src.models.tile import Tile
from src.models.constant import Color

from src.controllers.tile_controller import TileController


class Node:

    _id: Tuple[int, int]

    _g: int
    _h: int
    _f: int

    def __init__(self, id:  Tuple[int, int], g: int, h: int):
        self._id = id
        self._g = g
        self._h = h
        self._f = g + h

    def id(self) -> Tuple[int, int]:
        return self._id

    def g(self) -> int:
        return self._g

    def h(self) -> int:
        return self._h
    
    def f(self) -> int:
        return self._f


class BoardController:

    _board: Board

    def __init__(self, board: Board):
        self._board = board

    def set_last_move(self, tile: Tile):
        if tile.is_lock():
            self._board.set_last_move(tile)
            self._board.increment_move_count()
            self._board.current()

    def undo(self, current_player: Player):
        number_moves: int = self._board.move_count()
        if number_moves > 0 and self._board.is_current():
            last_tile: Tile = self._board.last_move()
            tile_controler = TileController(last_tile)

            if self._board.is_swapped() and self._board.move_count() == 1:    
                tile_controler.set_color(current_player.color())
                self._board.unswapped()
            else:
                self._board.decrement_move_count()
                tile_controler.reset()
                self._board.not_current()

    def hint(self, current_player: Player):
        empty_tile: List[List[Tile]] = list(filter(
            lambda t: not t.is_lock(),
            [tile for row in self._board.matrix() for tile in row]
        ))

        random_tile = choice(empty_tile)

        tile_controller = TileController(random_tile)

        tile_controller.on_player_clicked(current_player)
        self.set_last_move(random_tile)

    def swap_first_tile(self, current_player: Player):

        if self._board.move_count() == 1 and not self._board.is_swapped():
            first_tile: Tile = self._board.last_move()
            tile_controler = TileController(first_tile)
            tile_controler.set_color(current_player.color())
            self._board.swapped()

    # https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
    def check_win(self) -> bool:
        last_tile: Tile = self._board.last_move()

        edge_nodes: List[Node] = []

        for direction in last_tile.heuristics().keys():

            open_list: List[Node] = [
                Node(last_tile.id(), 0, last_tile.heuristics()[direction])
            ]
            closed_list: List[Tuple[int, int]] = []

            while len(open_list) > 0:
                open_list.sort(key = lambda node: node.f())
                current_node = open_list.pop()
                closed_list.append(current_node.id())

                if current_node.h() == 0:
                    edge_nodes.append(current_node.id())

                curent_tile: Tile =  self._board.find_tile(*current_node.id())
                for neighbor in curent_tile.neighbors():
                    tile: Tile =  self._board.find_tile(*neighbor)
                    if tile.color() == curent_tile.color() and tile.id() not in closed_list:
                        open_list.append(
                            Node(tile.id(), current_node.g() + 1, tile.heuristics()[direction])
                        )

        index: int = 0 if last_tile.color() == Color.RED else 1
        unique_indices: Tuple[int] = set(
            [node[index] for node in edge_nodes if node[index] == 0 or node[index] == 10]
        )

        if len(unique_indices) >= 2:
            self._board.set_game_over()
            for row in self._board.matrix():
                for tile in row:
                    tile_controller: TileController = TileController(tile)
                    tile_controller.lock()

    def reset(self):
        self._board.reset()
