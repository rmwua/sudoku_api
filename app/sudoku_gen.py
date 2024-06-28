from math import sqrt

from sudoku import Sudoku


class SudokuGen:

    @staticmethod
    def generate(width, difficulty):
        """
        Returns a random Sudoku puzzle with given width and difficulty.
        :param width: int
        :param difficulty: float
        :return:
        """
        puzzle = Sudoku(width=width, difficulty=difficulty)
        return puzzle.board

    @staticmethod
    def solve(arr: list[int], width: int = 3, height: int = 3) -> list[list[int]] or None:
        board = Board.transform_into_board(arr=arr)
        if board is None:
            return None
        board = Board.transform_into_board(arr=arr)
        puzzle = Sudoku(width=width, height=height, board=board)
        if puzzle.validate() is False or not board:
            return None
        return puzzle.solve().board

    @staticmethod
    def validate(arr: list[int], width: int = 3, height: int = 3) -> bool:
        board = Board.transform_into_board(arr=arr)
        if board is None:
            return False
        board = Board.transform_into_board(arr=arr)
        if not board:
            return False
        try:
            puzzle = Sudoku(width=width, height=height, board=board)
        except (IndexError, TypeError, ValueError):
            return False
        return puzzle.validate()

    @staticmethod
    def generate_custom(arr: list[int], width: int = 3, height: int = 3) -> list[list[int]] or None:
        board = Board.transform_into_board(arr=arr)


class Board:
    valid_lengths = (16, 81, 256)

    @staticmethod
    def transform_into_board(arr: list[int]) -> list[list[int]]:
        """
        Transforms array into 2D array
        :return: List[List[int]]
        """
        if Board.__validate(arr):
            board = []
            board_len = len(arr)
            num_cells = int(sqrt(board_len))
            for _cell in range(0, board_len, num_cells):
                cell = []
                for square in range(num_cells):
                    cell.append(arr[square + _cell])
                board.append(cell)
            return board

    @classmethod
    def __validate(cls, arr) -> bool:
        if arr is None:
            return False
        if len(arr) not in cls.valid_lengths:
            return False
        return True
