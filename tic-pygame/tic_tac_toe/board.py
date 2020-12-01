import pygame

from .constants import ROWS, COLS, SQUARE_SIZE, BLACK, WHITE, SQUARE_PADDING, BOARD_PADDING_LEFT, BOARD_PADDING_TOP
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
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(COLS):
                x = col * SQUARE_SIZE + col * SQUARE_PADDING + BOARD_PADDING_LEFT
                y = row * SQUARE_SIZE + row * SQUARE_PADDING + BOARD_PADDING_TOP
                pygame.draw.rect(win, WHITE, (x, y, SQUARE_SIZE, SQUARE_SIZE))

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                symbol = self.board[row][col]
                if symbol != 0:
                    symbol.draw(win)

    def move(self, row, col):
        self.board[row][col] = OSymbol(row, col)

