from copy import deepcopy
import pygame

from tic_tac_toe.constants import BLUE, RED


def minimax(board, depth, is_max_player):
    if depth == 0 or board.winner() or board.white_space == 0:
        return board.evaluate(is_max_player), board

    if is_max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_boards(board, BLUE):
            board_score = minimax(move, depth - 1, False)[0]
            max_eval = max(max_eval, board_score)
            if max_eval == board_score:
                best_move = move

        return max_eval, best_move

    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_boards(board, RED):
            board_score = minimax(move, depth - 1, True)[0]
            min_eval = min(min_eval, board_score)
            if min_eval == board_score:
                best_move = move

        return min_eval, best_move


def simulate_move(board, move, color):
    board.move(move[0], move[1], color)
    return board


def get_all_boards(board, color):
    boards = list()

    valid_moves = board.get_valid_moves()
    for move in valid_moves:
        temp_board = deepcopy(board)
        new_board = simulate_move(temp_board, move, color)
        boards.append(new_board)

    return boards
