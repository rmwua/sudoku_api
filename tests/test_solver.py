import random
import unittest

from app.sudoku_gen import SudokuGen, Board


class TestGenerator(unittest.TestCase):
    valid_unsolved = [0, 0, 7, 0, 4, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 8, 0, 0, 6,
                      0, 4, 1, 0, 0, 0, 9, 0, 0,
                      0, 0, 0, 0, 0, 0, 1, 7, 0,
                      0, 0, 0, 0, 0, 6, 0, 0, 0,
                      0, 0, 8, 7, 0, 0, 2, 0, 0,
                      3, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 1, 2, 0, 0, 0, 0,
                      8, 6, 0, 0, 7, 0, 0, 0, 5]

    solved = [[9, 8, 7, 6, 4, 2, 5, 3, 1],
              [2, 3, 5, 9, 1, 8, 7, 4, 6],
              [6, 4, 1, 5, 3, 7, 9, 8, 2],
              [5, 2, 6, 3, 8, 4, 1, 7, 9],
              [1, 7, 3, 2, 9, 6, 8, 5, 4],
              [4, 9, 8, 7, 5, 1, 2, 6, 3],
              [3, 1, 9, 8, 6, 5, 4, 2, 7],
              [7, 5, 4, 1, 2, 3, 6, 9, 8],
              [8, 6, 2, 4, 7, 9, 3, 1, 5]]

    def test_generate(self):
        puzzle = SudokuGen.generate(width=3, difficulty=0.6)[0]
        self.assertEqual(len(puzzle), 9)

    def test_solve(self):
        board = self.valid_unsolved

        result = SudokuGen.solve(board)
        self.assertEqual(result, self.solved)

    def test_solve_nan(self):
        board = None
        board2 = [random.randint(1, 9) for _ in range(10)]
        result = SudokuGen.solve(board)
        result2 = SudokuGen.solve(board2)
        self.assertEqual(result, None)
        self.assertEqual(result2, None)

    def test_validate(self):
        board = self.valid_unsolved
        board2 = None
        board3 = [1, 2, 3]
        result = SudokuGen.validate(board)
        result2 = SudokuGen.validate(board2)
        result3 = SudokuGen.validate(board3)
        # self.assertEqual(result, True)
        self.assertEqual(result2, False)
        self.assertEqual(result3, False)

    def test_generate_custom_board(self):
        board = self.valid_unsolved

    def test_board_to_2d(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7]
        arr2 = [1, 4, 5]
        result = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [4, 5, 6, 7]]
        result2 = None
        board = Board.transform_into_board(arr)
        board2 = Board.transform_into_board(arr2)
        self.assertEqual(result, board)
        self.assertEqual(result2, board2)
