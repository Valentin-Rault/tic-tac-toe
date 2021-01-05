import pygame

from tic_tac_toe.constants import WIDTH, HEIGHT, SQUARE_SIZE, SQUARE_PADDING, \
                                  BOARD_PADDING_TOP, BOARD_PADDING_LEFT, RED
from tic_tac_toe.game import Game
from minimax.algorithm import minimax

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')


def get_row_col_from_mouse(x, y):
    row = (y - BOARD_PADDING_TOP) // (SQUARE_SIZE + SQUARE_PADDING)
    col = (x - BOARD_PADDING_LEFT) // (SQUARE_SIZE + SQUARE_PADDING)
    return row, col


def main():
    clock = pygame.time.Clock()
    game = Game(WIN)

    while game.is_active:
        clock.tick(FPS)

        if game.turn == RED:
            _, new_board = minimax(game.get_board(), 3, False)
            game.ai_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.is_active = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(x, y)
                game.is_active = game.play(row, col)

        game.update()

    pygame.quit()


main()
