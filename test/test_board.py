import unittest
import sys

sys.path.append('../reversi')
from reversi import board  # noqa


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = board.Board()

    def test_init_board(self):
        correct_pieces = [['', '', '', '', '', '', '', ''],
                          ['', '', '', '', '', '', '', ''],
                          ['', '', '', '', '', '', '', ''],
                          ['', '', '', 'b', 'w', '', '', ''],
                          ['', '', '', 'w', 'b', '', '', ''],
                          ['', '', '', '', '', '', '', ''],
                          ['', '', '', '', '', '', '', ''],
                          ['', '', '', '', '', '', '', '']]
        self.assertEqual(self.board.pieces, correct_pieces)

    def test_can_place_piece(self):
        can_place_piece = self.board.can_place_piece('w')
        self.assertTrue(can_place_piece)

    def test_get_winner_draw(self):
        winner = self.board.get_winner()
        self.assertEqual(winner, '')

    def test_get_winner_white(self):
        self.board.pieces[3][3] = 'w'
        self.board.pieces[2][3] = 'w'
        winner = self.board.get_winner()
        self.assertEqual(winner, 'w')

    def test_place_piece_not_empty(self):
        self.assertRaises(ValueError, self.board.place_piece, 'w', 3, 3)

    def test_place_piece_not_reversing(self):
        self.assertRaises(ValueError, self.board.place_piece, 'w', 3, 5)

    def test_place_piece_reversing(self):
        self.board.place_piece('w', 3, 2)
        self.assertEqual(self.board.pieces[2][3], 'w', msg='place new piece')
        self.assertEqual(
            self.board.pieces[3][3], 'w', msg='reverse opponents piece')
