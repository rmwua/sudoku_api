from typing import Any, Union, Tuple

from flask import Blueprint, request, jsonify, Response
from .sudoku import Sudoku

main = Blueprint('main', __name__)


@main.route('/create_standard', methods=['GET'])
def create_standard() -> Response:
    """
    creates easy level sudoku puzzle
    :return:JSON response
    """
    sudoku = Sudoku.create_sudoku()
    return jsonify({"sudoku": sudoku})


@main.route('/create_level', methods=['POST'])
def create_level() -> Response | Tuple[Response, int]:
    """
    creates chosen by user level sudoku puzzle
    :return: JSON response
    """
    data = request.get_json()
    diff = data.get('difficulty')
    if diff not in [1, 2, 3]:
        return jsonify({"error": "Invalid difficulty level"}), 400
    sudoku = Sudoku.create_sudoku(diff=diff)
    return jsonify({"sudoku": sudoku})


@main.route('/create_custom', methods=['POST'])
def create_custom() -> Response | Tuple[Response, int]:
    """
    validates custom sudoku
    :return: JSON response
    """
    data = request.get_json()
    nums = data.get('nums')
    valid = Sudoku.check_valid(nums=nums)
    if not valid:
        return jsonify({"error": "Invalid custom numbers"}), 400
    sudoku = Sudoku.create_custom(nums=nums)
    return jsonify({"sudoku": sudoku})


@main.route('/solve', methods=['POST'])
def solve() -> Response | Tuple[Response, int]:
    """
    solves sudoku that is sent by user
    :return: JSON response
    """
    data = request.get_json()
    nums = data.get('nums')
    valid = Sudoku.check_valid(nums=nums)
    if not valid:
        return jsonify({"error": "Invalid sudoku"}), 400
    solved = Sudoku.solve(nums=nums)
    return jsonify({"solved": solved})


@main.route('/verify', methods=['POST'])
def verify() -> Response | Tuple[Response, int]:
    """
    verifies sudoku that is sent by user
    :return: JSON response
    """
    data = request.get_json()
    nums = data.get('nums')
    valid = Sudoku.check_valid(nums=nums)
    if not valid:
        return jsonify({"error": "Invalid sudoku"}), 400
    result = Sudoku.verify(nums=nums)
    return jsonify({"result": result})

