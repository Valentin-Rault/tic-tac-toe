import pygame

from .constants import WIDTH, ROWS, COLS, SQUARE_SIZE, BLACK, WHITE

SQUARE_PADDING = 5
BOARD_PADDING_LEFT = WIDTH // 4 - 2 * SQUARE_PADDING
BOARD_PADDING_TOP = 20

class Board:
    def __init__(self):
        self.board = []
        self.white_space = 9
        self.create_board()

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append('')

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(COLS):
                x = col * SQUARE_SIZE + col * SQUARE_PADDING + BOARD_PADDING_TOP
                y = row * SQUARE_SIZE + row * SQUARE_PADDING + BOARD_PADDING_LEFT
                pygame.draw.rect(win, WHITE, (y, x, SQUARE_SIZE, SQUARE_SIZE))

