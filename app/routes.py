from typing import Tuple
from flask import Blueprint, request, jsonify, Response
from .sudoku_gen import SudokuGen, Board

main = Blueprint('main', __name__)


@main.route('/generate/', methods=['GET'])
def generate() -> Response:
    """
    creates a sudoku puzzle with levels from 1 to 3
    and any width (min 2)

    :return:JSON response
    # """
    width = request.args.get("width", default=3, type=int)
    difficulty = request.args.get("difficulty", default=0.6, type=float)

    puzzle, solved = SudokuGen.generate(width=int(width), difficulty=float(difficulty))
    return jsonify({"sudoku": Board.printable_board(puzzle)},
                   {"solved": Board.printable_board(solved)})


@main.route('/solve', methods=['POST'])
def solve() -> Response | Tuple[Response, int]:
    """
    solves sudoku that is sent by user
    :return: JSON response
    """
    puzzle = request.get_json()['arr']
    if not puzzle:
        return jsonify({"error": "No puzzle provided"}), 400
    result = SudokuGen.solve(puzzle)
    if not result:
        return jsonify({"error": "No solution found"}), 400
    return jsonify(Board.printable_board(result))


@main.route('/validate', methods=['POST'])
def validate() -> Response | Tuple[Response, int]:
    """
    validates sudoku that is sent by user
    :return: JSON response
    """
    puzzle = request.get_json()['arr']
    if not puzzle:
        return jsonify({"error": "No puzzle provided"}), 400
    result = SudokuGen.validate(puzzle)
    return jsonify(result)
