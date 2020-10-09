import functools
import time
import random


def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)

    helper.calls = 0
    return helper


def start_game(filename):
    with open(filename, 'w') as f:
        f.truncate(0)
    game_active = True
    player_start = random.randint(1, 2)
    if player_start == 1:
        player = True
    else:
        player = False
    return player, game_active


def end_game(player):
    if player:
        user = 'The player'
    else:
        user = 'The bot'
    print(f'{user} won.')
    game_active = False
    return game_active, user


def switch_player(player):
    if player:
        player = False
    else:
        player = True
    return player


def check_win(player, game_active, board):
    if board['1'] != ' ':
        if board['1'] == board['2'] == board['3']:
            return end_game(player)
        elif board['1'] == board['4'] == board['7']:
            return end_game(player)

    if board['9'] != ' ':
        if board['9'] == board['6'] == board['3']:
            return end_game(player)
        elif board['9'] == board['8'] == board['7']:
            return end_game(player)

    if board['5'] != ' ':
        if board['5'] == board['2'] == board['8']:
            return end_game(player)
        elif board['5'] == board['4'] == board['6']:
            return end_game(player)
        elif board['5'] == board['1'] == board['9']:
            return end_game(player)
        elif board['5'] == board['3'] == board['7']:
            return end_game(player)

    return game_active, False


def compute_value(result, value):
    result += value
    if len(result) == 9 and ' ' not in result:
        print('It is a draw.')
        return 'draw'
    return result


def check_draw(game_active, board):
    if game_active:
        value = functools.reduce(compute_value, board.values(), '')
        if value == 'draw':
            game_active = False
    return game_active


# Called when testing recursion
# @call_counter
def get_input(player, board):
    if player:
        print("Player's turn")
        player_input = input('Enter a number: ')
        if not player_input.isdigit():
            print('Invalid input, please enter a number')
            return get_input(player, board)
        if int(player_input) <= 0 or int(player_input) > 9 or board[player_input] != ' ':
            print('Invalid input, please try again')
            return get_input(player, board)
        return player_input
    else:
        player_input = str(random.randint(1, 9))
        if board[player_input] != ' ':
            return get_input(player, board)
        return player_input


def play_token(player, game_active, filename, board):
    if not game_active:
        player, game_active = start_game(filename)
    move = get_input(player, board)
    if player:
        board[move] = 'x'
    else:
        print(f'Bot played: {move}')
        time.sleep(0.5)
        board[move] = 'o'
    board_state = show_board(board)
    print(show_board(board))
    game_active, user = check_win(player, game_active, board)
    game_active = check_draw(game_active, board)
    save_state(player, move, user, board_state, game_active, filename)
    player = switch_player(player)
    if game_active:
        return play_token(player, game_active, filename, board)


def save_state(player, move, user, board_state, game_active, filename):
    with open(filename, 'a') as f:
        f.write(f'PLayer played: {move}\n\n') if player else f.write(f'Bot played: {move}\n\n')
        f.write(board_state)
        f.write('\n\n')
        if not game_active:
            f.write(f'{user} won.') if user else f.write('It is a draw.')


def show_board(board):
    def concatenate_value(result, key):
        result += board[key]
        if int(key) % 3 != 0:
            result += '|'
        if int(key) % 3 == 0 and int(key) % 9 != 0:
            result += '\n' + '-----' + '\n'
        return result
    return functools.reduce(concatenate_value, board, '')


if __name__ == '__main__':
    DIGITS = map(str, (range(1, 10)))
    game_board = {key: ' ' for key in DIGITS}
    is_active = False
    play_token(False, is_active, 'tic_tac_toe_state.txt', game_board)
