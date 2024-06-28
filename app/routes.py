from typing import Any, Union, Tuple, Annotated

from flask import Blueprint, request, jsonify, Response
from .sudoku_gen import SudokuGen

# from sudoku import Sudoku

main = Blueprint('main', __name__)


@main.route('/generate/', methods=['GET'])
def generate() -> Response:
    """
    creates a sudoku puzzle with levels from 1 to 3
    and any width (min 2)

    :return:JSON response
    # """
    diff = request.args.get('diff') if request.args.get('level') is not None else 0.6
    width = request.args.get('width') if request.args.get('width') is not None else 3
    # puzzle = Sudoku(int(width)).difficulty(float(diff))
    puzzle = SudokuGen.generate(width=int(width), difficulty=int(diff))
    return jsonify(puzzle.__dict__["board"])


@main.route('/solve', methods=['GET'])
def solve() -> Response | Tuple[Response, int]:
    """
    solves sudoku that is sent by user
    :return: JSON response
    """
    puzzle = request.get_json()['arr']
    result = SudokuGen.solve(puzzle)
    return jsonify(result)


@main.route('/validate', methods=['GET'])
def verify() -> Response | Tuple[Response, int]:
    """
    validates sudoku that is sent by user
    :return: JSON response
    """
    puzzle = request.get_json()['arr']
    result = SudokuGen.validate(puzzle)
    return jsonify(result)
