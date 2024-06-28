from math import sqrt
from typing import Tuple, List, Any

from sudoku import Sudoku


class SudokuGen:

    @staticmethod
    def generate(width: int, difficulty: float) -> tuple[Any, Sudoku]:
        """
        Returns a random Sudoku puzzle with given width and difficulty and the solved version

        """
        puzzle = Sudoku(width=width).difficulty(difficulty=difficulty)
        return puzzle.board, puzzle.solve().board

    @staticmethod
    def solve(arr: list[int]) -> list[list[int]] or None:
        """
        Solves the Sudoku puzzle with given width and height.
        arr: list of ints, line by line sudoku

        """
        board = Board.transform_into_board(arr=arr)
        if board is None:
            return None
        height, width = int(sqrt(len(board))), int(sqrt(len(board)))
        puzzle = Sudoku(width=width, height=height, board=board)
        if puzzle.validate() is False or not board:
            return None
        print(puzzle.show())
        return puzzle.solve().board

    @staticmethod
    def validate(arr: list[int]) -> bool:
        """
        Validates the Sudoku puzzle with given width and height.

        """
        board = Board.transform_into_board(arr=arr)
        if board is None:
            return False
        height, width = len(board), len(board)
        try:
            puzzle = Sudoku(width=width, height=height, board=board)
        except (IndexError, TypeError, ValueError):
            return False
        return puzzle.validate()


    @staticmethod
    def generate_custom(arr: list[int],) -> list[list[int]] or None:
        board = Board.transform_into_board(arr=arr)
        if board:
            return Board.printable_board(board=board)


class Board:
    valid_lengths = (16, 81, 256)

    @staticmethod
    def transform_into_board(arr: list[int]) -> list[list[int]]:
        """
        Transforms array into 2D array

        """
        if Board.validate(arr):
            board = []
            board_len = len(arr)
            num_cells = int(sqrt(board_len))
            for _cell in range(0, board_len, num_cells):
                cell = []
                for square in range(num_cells):
                    cell.append(arr[square + _cell])
                board.append(cell)
            return board

    @staticmethod
    def transform_into_arr(board: list[list[int]]) -> list[int]:
        """
        Transforms board into 1D array

        """
        arr = [square for cell in board for square in cell]
        return arr

    @staticmethod
    def printable_board(board: list[list[int]] or Sudoku):
        table = ''
        width, height = int(sqrt(len(board))), int(sqrt(len(board)))
        size = width * height
        cell_length = 1

        format_int = '{0:0' + str(cell_length) + 'd}'
        for i, row in enumerate(board):
            if i == 0:
                table += ('+-' + '-' * (cell_length + 1) * width) * height + '+' + '\n'
            table += (('| ' + '{} ' * width) * height + '|').format(
                    *[format_int.format(x) if x is not None else ' ' * cell_length for x in row]) + '\n'
            if i == size - 1 or i % height == height - 1:
                table += ('+-' + '-' * (cell_length + 1) *
                          width) * height + '+' + '\n'

        return table

    @classmethod
    def validate(cls, arr) -> bool:
        if arr is None:
            return False
        if len(arr) not in cls.valid_lengths:
            return False
        return True

