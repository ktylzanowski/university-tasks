import unittest
import queens as q


class TestQueens(unittest.TestCase):

    def test_generate_board(self):
        board = q.generate_board()
        self.assertEqual(len(board), 8)
        for row in board:
            self.assertEqual(len(row), 8)

    def test_is_pawn_in_danger(self):

        #         [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        #          ['Q', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        #          [' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' '],
        #          [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' '],
        #          [' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' '],
        #          [' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' '],
        #          [' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' '],
        #          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

        queens = [(1, 0), (2, 2), (4, 3), (5, 1), (6, 4)]
        pawn = (3, 3)
        self.assertEqual(q.is_pawn_in_danger(queens, pawn), [(2, 2), (4, 3), (5, 1)])
