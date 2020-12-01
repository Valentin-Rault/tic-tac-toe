import pygame

from .constants import BLUE, RED, WHITE, SQUARE_SIZE, SQUARE_PADDING, BOARD_PADDING_TOP, BOARD_PADDING_LEFT


class Symbol:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = BLUE
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = self.col * SQUARE_SIZE + self.col * SQUARE_PADDING + BOARD_PADDING_LEFT + SQUARE_SIZE // 2
        self.y = self.row * SQUARE_SIZE + self.row * SQUARE_PADDING + BOARD_PADDING_TOP + SQUARE_SIZE // 2


class XSymbol(Symbol):
    def __init__(self, row, col):
        super().__init__(row, col)

    def draw(self, win):
        pygame.draw.line(win, BLUE,  (self.x - 38, self.y - 38), (self.x + 38, self.y + 38), 10)
        pygame.draw.line(win, BLUE,  (self.x + 38, self.y - 38), (self.x - 38, self.y + 38), 10)


class OSymbol(Symbol):
    def __init__(self, row, col):
        super().__init__(row, col)

    def draw(self, win):
        pygame.draw.circle(win, RED, (self.x, self.y), 48)
        pygame.draw.circle(win, WHITE, (self.x, self.y), 38)