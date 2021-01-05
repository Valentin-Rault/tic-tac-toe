import pygame

from .constants import ROWS, COLS, SQUARE_SIZE, WHITE, BLUE, RED,\
                       SQUARE_PADDING, BOARD_PADDING_LEFT, BOARD_PADDING_TOP
from .symbols import XSymbol, OSymbol, EmptySymbol


class Board:
    def __init__(self):
        self.board = []
        self.white_space = 9
        self.create_board()

    def __repr__(self):
        return str(self.board)

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(EmptySymbol())

    def draw_squares(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                x = col * SQUARE_SIZE + col * SQUARE_PADDING + BOARD_PADDING_LEFT
                y = row * SQUARE_SIZE + row * SQUARE_PADDING + BOARD_PADDING_TOP
                pygame.draw.rect(win, WHITE, (x, y, SQUARE_SIZE, SQUARE_SIZE))

    def highlight_selected(self, win, row, col, turn):
        x = col * SQUARE_SIZE + col * SQUARE_PADDING + BOARD_PADDING_LEFT
        y = row * SQUARE_SIZE + row * SQUARE_PADDING + BOARD_PADDING_TOP
        pygame.draw.rect(win, turn, (x - SQUARE_PADDING,
                                     y - SQUARE_PADDING,
                                     SQUARE_SIZE + 2 * SQUARE_PADDING,
                                     SQUARE_SIZE + 2 * SQUARE_PADDING))

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                symbol = self.board[row][col]
                if symbol.color is not None:
                    symbol.draw(win)

    def move(self, row, col, turn):
        if turn == BLUE:
            self.board[row][col] = XSymbol(row, col, turn)
        elif turn == RED:
            self.board[row][col] = OSymbol(row, col, turn)

        self.white_space -= 1

    def get_value_color(self, row, col):
        if row < 0 or col < 0:
            return True
        return self.board[row][col].color

    def evaluate(self, is_max_player):
        score = 0
        if self.winner() and not is_max_player:
            score = 1
        elif self.winner() and is_max_player:
            score = -1
        return score

    def get_valid_moves(self):
        moves = []
        for row in range(ROWS):
            for col in range(COLS):
                symbol = self.board[row][col]
                if symbol.color is None:
                    moves.append((row, col))
        return moves

    def is_move_left(self):
        if self.white_space > 0:
            return True
        return False

    def winner(self):
        if self.board[0][0].color == self.board[1][1].color == self.board[2][2].color \
                and self.board[0][0].color is not None:
            return True
        elif self.board[0][2].color == self.board[1][1].color == self.board[2][0].color \
                and self.board[0][2].color is not None:
            return True
        else:
            for row in range(ROWS):
                if self.board[row][0].color == self.board[row][1].color == self.board[row][2].color \
                        and self.board[row][0].color is not None:
                    return True
            for col in range(COLS):
                if self.board[0][col].color == self.board[1][col].color == self.board[2][col].color \
                        and self.board[0][col].color is not None:
                    return True

        return False
