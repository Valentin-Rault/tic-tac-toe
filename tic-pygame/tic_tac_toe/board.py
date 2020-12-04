import pygame

from .constants import ROWS, COLS, SQUARE_SIZE, WHITE, BLUE, RED,\
                       SQUARE_PADDING, BOARD_PADDING_LEFT, BOARD_PADDING_TOP
from .symbols import XSymbol, OSymbol


class Board:
    def __init__(self):
        self.board = []
        self.white_space = 9
        self.create_board()

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)

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
                if symbol != 0:
                    symbol.draw(win)

    def move(self, row, col, turn):
        if turn == BLUE:
            self.board[row][col] = XSymbol(row, col, turn)
        elif turn == RED:
            self.board[row][col] = OSymbol(row, col, turn)

        self.white_space -= 1

    def get_value(self, row, col):
        if row < 0 or col < 0:
            return True
        return self.board[row][col]

    def is_move_left(self):
        if self.white_space > 0:
            return True
        return False

    def winner(self):
        if type(self.board[0][0]) == type(self.board[1][1]) == type(self.board[2][2]) and not isinstance(self.board[0][0], int):
            return True
        elif type(self.board[0][2]) == type(self.board[1][1]) == type(self.board[2][0]) and not isinstance(self.board[0][2], int):
            return True
        else:
            for row in range(ROWS):
                if type(self.board[row][0]) == type(self.board[row][1]) == type(self.board[row][2]) and not isinstance(self.board[row][0], int):
                    return True
            for col in range(COLS):
                if type(self.board[0][col]) == type(self.board[1][col]) == type(self.board[2][col]) and not isinstance(self.board[0][col], int):
                    return True
