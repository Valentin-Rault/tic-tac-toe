import pygame

from .constants import BLUE, RED
from .board import Board


class Game:
    def __init__(self, win):
        self.win = win
        self.board = Board()
        self.turn = BLUE
        self.selected_row_col = None

    def change_turn(self):
        if self.turn == BLUE:
            self.turn = RED
        else:
            self.turn = BLUE

    def select_square(self, row, col):
        if self.selected_row_col:
            result = self.confirm_move(row, col)
            if result:
                self.board.move(row, col, self.turn)
                self.change_turn()
                self.selected_row_col = None
                return True
            else:
                self.selected_row_col = None
                self.select_square(row, col)

        if self.board.get_value(row, col) == 0:
            self.selected_row_col = row, col

    def confirm_move(self, row, col):
        if (row, col) == self.selected_row_col:
            return True
        return False

    def highlight_selected(self):
        pass

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def play(self, row, col):
        is_move = self.select_square(row, col)
        if is_move:
            is_winner = self.board.winner()
            if not is_winner:
                is_move_left = self.board.is_move_left()
                if not is_move_left:
                    print('It is a draw')
                    return False
            else:
                print('Winner')
                return False
        return True
