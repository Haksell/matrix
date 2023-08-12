from classes import Vector
from functions import linear_combination


def test_linear_combination_valid():
    assert linear_combination([], []) == Vector([])
    assert linear_combination([Vector([1, 2, 3])], [-1]) == Vector([-1, -2, -3])
    assert linear_combination([Vector([1, 2, 3])], [0]) == Vector([0, 0, 0])
    assert linear_combination([Vector([1, 2, 3])], [1]) == Vector([1, 2, 3])
    assert linear_combination([Vector([1, 2, 3])], [2]) == Vector([2, 4, 6])
    assert linear_combination([Vector([1, 2, 3]), Vector([4, 5, 6])], [7, 8]) == Vector(
        [39, 54, 69]
    )
    assert linear_combination(
        [Vector([1, 2, 3]), Vector([2, 4, 6])], [2, -1]
    ) == Vector([0, 0, 0])
