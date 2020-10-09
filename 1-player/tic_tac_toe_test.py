import unittest
import os
from unittest import mock

# from parameterized import parameterized, parameterized_class
# TODO: install and check doc parameterized
# TODO: list problem for python bloc post about common python problems

import tic_tac_toe as ts


class TicStartTest(unittest.TestCase):

    def setUp(self):
        self.player = False
        self.game_active = False
        self.filename = 'tic_test.txt'
        self.start_player, self.start_game = ts.start_game(self.player, self.game_active, self.filename)

    def tearDown(self):
        os.remove(self.filename)

    def test_player_true(self):
        if self.start_player:
            self.assertTrue(self.start_player)

    def test_player_false(self):
        if not self.start_player:
            self.assertFalse(self.start_player)

    def test_game_active(self):
        self.assertTrue(self.start_game)

    def test_creation_file(self):
        with open(self.filename) as f:
            file = f.readlines()
        self.assertEqual(file, [])


class TicEndTest(unittest.TestCase):

    def setUp(self):
        self.player = True
        self.game_active = True
        self.end_game, self.user = ts.end_game(self.player, self.game_active)

    def test_game_inactive(self):
        self.assertFalse(self.end_game)

    def test_user_player(self):
        self.assertEqual(self.user, 'The player')

    def test_user_bot(self):
        self.player = False
        end_game = ts.end_game(self.player, self.game_active)
        self.assertEqual(end_game, (False, 'The bot'))


class TicPlayerTest(unittest.TestCase):

    def test_player_true(self):
        player = False
        self.assertTrue(ts.switch_player(player))

    def test_player_false(self):
        player = True
        self.assertFalse(ts.switch_player(player))


# @parameterized_class(('board',), [({'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ',
#                                   '7': ' ', '8': ' ', '9': ' '},)])
class WinTest(unittest.TestCase):

    def setUp(self):
        self.player = True
        self.game_active = True
        digits = map(str, (range(1, 10)))
        self.board = {key: ' ' for key in digits}

    def test_game_active_user_false(self):
        result = ts.check_win(self.player, self.game_active, self.board)
        self.assertEqual(result, (True, False))

    # @ parameterized.expand(('board["1"]', 'board["2"]', 'board["3"]', 'board["4"]', 'board["5"]', 'board["6"]',
    #                 'board["7"]', 'board["8"]', 'board["9"]'), [
    #     ('x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ')
    # ])
    # @ parameterized.expand('board', [{'1': 'x', '2': 'x', '3': 'x', '4': ' ', '5': ' ', '6': ' ',
    #                              '7': ' ', '8': ' ', '9': ' '}])
    def test_win_board_1_1(self):
        self.board['1'] = self.board['2'] = self.board['3'] = 'x'
        self.assertEqual(ts.check_win(self.player, self.game_active, self.board), (False, 'The player'))

    def test_win_board_1_4(self):
        self.board['1'] = self.board['4'] = self.board['7'] = 'x'
        self.assertEqual(ts.check_win(self.player, self.game_active, self.board), (False, 'The player'))

    def test_win_board_9_6(self):
        self.board['9'] = self.board['6'] = self.board['3'] = 'x'
        self.assertEqual(ts.check_win(self.player, self.game_active, self.board), (False, 'The player'))

    def test_win_board_9_8(self):
        self.board['9'] = self.board['8'] = self.board['7'] = 'x'
        self.assertEqual(ts.check_win(self.player, self.game_active, self.board), (False, 'The player'))

    def test_win_board_5_1(self):
        self.board['5'] = self.board['1'] = self.board['9'] = 'x'
        self.assertEqual(ts.check_win(self.player, self.game_active, self.board), (False, 'The player'))

    def test_win_board_5_2(self):
        self.board['5'] = self.board['2'] = self.board['8'] = 'x'
        self.assertEqual(ts.check_win(self.player, self.game_active, self.board), (False, 'The player'))

    def test_win_board_5_3(self):
        self.board['5'] = self.board['3'] = self.board['7'] = 'x'
        self.assertEqual(ts.check_win(self.player, self.game_active, self.board), (False, 'The player'))

    def test_win_board_5_4(self):
        self.board['5'] = self.board['4'] = self.board['6'] = 'x'
        self.assertEqual(ts.check_win(self.player, self.game_active, self.board), (False, 'The player'))


class DrawTest(unittest.TestCase):

    def setUp(self):
        self.game_active = True

    def test_not_draw(self):
        digits = map(str, (range(1, 10)))
        board = {key: ' ' for key in digits}
        self.assertTrue(ts.check_draw(self.game_active, board))

    def test_draw(self):
        digits = map(str, range(1, 10))
        board = {key: 'x' for key in digits}
        self.assertFalse(ts.check_draw(self.game_active, board))


class InputPlayerBot(unittest.TestCase):

    def setUp(self):
        self.player = True
        self.digits = list(map(str, range(1, 10)))
        self.board = {key: ' ' for key in self.digits}

    @mock.patch('builtins.input', side_effect=['1', 'a', '2', '3'])
    def test_wrong_input(self, input):
        self.board['1'] = 'x'
        output = ts.get_input(self.player, self.board)
        self.assertEqual(ts.get_input.calls, 3)
        self.assertIn(ts.get_input(self.player, self.board), self.digits)

    digits_string = '1 2 3 4 5 6 7 8 9'

    @mock.patch('builtins.input', side_effect=digits_string)
    def test_all_input(self, input):
        output = ts.get_input(self.player, self.board)
        self.assertIn(output, self.digits)

    def test_bot_input(self):
        self.player = False
        self.board = {key: 'x' for key in self.board.keys()}
        self.board['2'] = ' '
        self.assertIn(ts.get_input(self.player, self.board), self.digits)


startSuite = unittest.TestSuite()
startSuite.addTests([
    TicStartTest('test_player_true'), TicStartTest('test_player_false'),
    TicStartTest('test_game_active'), TicStartTest('test_creation_file')
])

endSuite = unittest.TestSuite()
endSuite.addTests([
    TicEndTest('test_game_inactive'), TicEndTest('test_user_player'), TicEndTest('test_user_bot')
])

playerSuite = unittest.TestSuite()
playerSuite.addTests([
    TicPlayerTest('test_player_true'), TicPlayerTest('test_player_false')
])

inputSuite = unittest.TestSuite()
inputSuite.addTests([
    InputPlayerBot('test_wrong_input'), InputPlayerBot('test_all_input'),
    InputPlayerBot('test_bot_input')
])

winSuite = unittest.TestSuite()
winSuite.addTests([
    WinTest('test_game_active_user_false'), WinTest('test_win_board_1_1'), WinTest('test_win_board_1_4'),
    WinTest('test_win_board_9_6'), WinTest('test_win_board_9_8'), WinTest('test_win_board_5_1'),
    WinTest('test_win_board_5_2'), WinTest('test_win_board_5_3'), WinTest('test_win_board_5_4')
])

drawSuite = unittest.TestSuite()
drawSuite.addTests([
    DrawTest('test_not_draw'), DrawTest('test_draw')
])
