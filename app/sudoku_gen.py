from sudoku import Sudoku
import copy


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
    def solve(arr: list[list[int]]) -> list[list[int]] or None:
        if arr is None:
            return None
        puzzle = Sudoku(3, 3, board=arr)
        if puzzle.validate() is False:
            return None
        return puzzle.solve().board

    @staticmethod
    def validate(arr: list[list[int]]) -> bool:
        if arr is None:
            return False
        try:
            puzzle = Sudoku(3, 3, board=arr)
        except (IndexError, TypeError, ValueError):
            return False
        return puzzle.validate()
