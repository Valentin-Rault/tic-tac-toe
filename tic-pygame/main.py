import pygame

from tic_tac_toe.constants import WIDTH, HEIGHT, SQUARE_SIZE, SQUARE_PADDING, BOARD_PADDING_TOP, BOARD_PADDING_LEFT
from tic_tac_toe.board import Board
from tic_tac_toe.game import Game

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')


def get_row_col_from_mouse(x, y):
    row = (y - BOARD_PADDING_TOP) // (SQUARE_SIZE + SQUARE_PADDING)
    col = (x - BOARD_PADDING_LEFT) // (SQUARE_SIZE + SQUARE_PADDING)
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(x, y)
                run = game.play(row, col)

        game.update()
        pygame.display.update()

    pygame.quit()


main()
