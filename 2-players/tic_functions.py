"""Module containing the core functions for tic tac toe"""
import functools
import random

from tic_player import Player


player1 = Player('x', 'Player 1')
player2 = Player('o', 'Player 2')


def start_game(clients):
    """Assign clients address and nickname to players"""
    if not player1.client and not player2.client:
        player1.client = random.choice(list(clients.keys()))
        player1.nickname = clients[player1.client]
        del clients[player1.client]
        player2.client = list(clients.keys())[0]
        player2.nickname = clients[player2.client]
    return player1, player2


def switch_player(players, active_player):
    """Switches between both players"""
    for player in players:
        if player == active_player:
            players.remove(player)
    return players[0]


def check_win(game_active, board):
    """Checks the board to find 3 symbols in a row/column/diagonal"""
    result = False
    if board['1'] != ' ':
        if board['1'] == board['2'] == board['3'] or board['1'] == board['4'] == board['7']:
            result = True
            game_active = False

    if board['5'] != ' ':
        if board['5'] == board['2'] == board['8'] or board['5'] == board['4'] == board['6']:
            result = True
            game_active = False
        elif board['5'] == board['1'] == board['9'] or board['5'] == board['3'] == board['7']:
            result = True
            game_active = False

    if board['9'] != ' ':
        if board['9'] == board['6'] == board['3'] or board['9'] == board['8'] == board['7']:
            result = True
            game_active = False

    return result, game_active


def compute_value(result, value):
    """Checks the board if no empty space and no win, returns draw"""
    result += value
    if len(result) == 9 and ' ' not in result:
        return 'draw'
    return result


def check_draw(game_active, board):
    """If no win checks for a draw"""
    message = ''
    if game_active:
        value = functools.reduce(compute_value, board.values(), '')
        if value == 'draw':
            game_active = False
            message = 'It is a draw'
    return message, game_active


def show_board(board):
    """Iterates over the dictionary to assemble the board"""
    def concatenate_value(result, key):
        """Assemble the dictionary values with the board's lines"""
        result += board[key]
        if int(key) % 3 != 0:
            result += '|'
        elif int(key) % 3 == 0 and int(key) % 9 != 0:
            result += '\n' + '-----' + '\n'
        return result
    return functools.reduce(concatenate_value, board, '')


def validate_input(player, board):
    """Accepts an input and validates it"""
    player.send('PLease enter a number: '.encode('utf-8'))
    move = player.recv(1024).decode('utf-8')
    if not move.isdigit():
        player.send('Incorrect input'.encode('utf-8'))
        return validate_input(player, board)
    elif int(move) <= 0 or int(move) > 9 or board[move] != ' ':
        player.send('Incorrect input, try again'.encode('utf-8'))
        return validate_input(player, board)
    return move
