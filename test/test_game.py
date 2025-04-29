import unittest
from unittest import mock
import sys

sys.path.append('../reversi')
from reversi import game  # noqa


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = game.Game()
        self.game.board.place_piece = mock.Mock()

    def test_not_passed_can_place(self):
        '''
        No player has passed and the opponent can place.
        => It is the opponents turn.
        '''
        self.game.board.can_place_piece = mock.Mock(return_value=True)
        self.game.make_move(0, 0)
        self.assertEqual(self.game.current_player, 'w')

    def test_not_passed_can_not_place(self):
        '''
        No player has passed and the opponent can not place.
        => The opponent passes. It is the same players turn.
        '''
        self.game.board.can_place_piece = mock.Mock()
        self.game.board.can_place_piece.side_effect = [False, True]
        self.game.make_move(0, 0)
        self.assertEqual(self.game.current_player, 'b',
                         msg='same player after passing')
        self.assertTrue(self.game.player_has_passed, msg='player has passed')

    def test_passed_can_place(self):
        '''
        A player has passed and the player can place again.
        => It is the same players turn.
        '''
        self.game.player_has_passed = True
        self.game.board.can_place_piece = mock.Mock(return_value=True)
        self.game.make_move(0, 0)
        self.assertEqual(self.game.current_player, 'b')

    def test_passed_opponent_can_place(self):
        '''
        A player has passed, the player can not place but the opponent can.
        => It is the opponents turn.
        '''
        self.game.player_has_passed = True
        self.game.board.can_place_piece = mock.Mock()
        self.game.board.can_place_piece.side_effect = [False, True]
        self.game.make_move(0, 0)
        self.assertEqual(self.game.current_player, 'w')

    def test_passed_can_not_place(self):
        '''
        A player has passed and both players can not place.
        => The game is over.
        '''
        self.game.player_has_passed = True
        self.game.board.can_place_piece = mock.Mock(return_value=False)
        self.game.make_move(0, 0)
        self.assertEqual(self.game.current_player, '')
