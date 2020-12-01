import pygame

from tic_tac_toe.constants import WIDTH, HEIGHT
from tic_tac_toe.board import Board

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        board.draw_squares(WIN)
        pygame.display.update()

    pygame.quit()


main()
