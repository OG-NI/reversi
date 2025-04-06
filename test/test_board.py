import unittest
import sys
sys.path.append('..')
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
        print(correct_pieces)
        self.assertEqual(self.board.pieces, correct_pieces)


if __name__ == "__main__":
    unittest.main()
