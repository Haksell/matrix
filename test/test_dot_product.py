# TODO: test V@V V@M M@V V@V with complex numbers

import pytest
from src import Matrix, Vector


def test_matmul():
    A = Vector([1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j])
    B = Vector([3 - 4j, 6 - 2j, 1 + 2j, 4 + 3j])
    assert A @ A == 8
    assert A @ B == 1 - 5j
    assert B @ A == 1 + 5j
    assert B @ B == 95
    assert Vector([1, 2, 3]) @ Vector([1, 2, 3]) == 14
    assert Vector([1, 0]) @ Vector([0, 1]) == 0
    assert Vector([1, 2]) @ Matrix([[1, 2, 3], [4, 5, 6]]) == Vector([9, 12, 15])
    with pytest.raises(Exception):
        Vector([1, 2]) @ Vector([1, 2, 3])


def test_mat_vec():
    assert Matrix([[1, 0], [0, 1]]).mul_vec(Vector([4, 2])) == Vector([4, 2])
    assert Matrix([[2, 0], [0, 2]]).mul_vec(Vector([4, 2])) == Vector([8, 4])
    assert Matrix([[2, -2], [-2, 2]]).mul_vec(Vector([4, 2])) == Vector([4, -4])
    with pytest.raises(Exception):
        Matrix([[1, 0], [0, 1]]).mul_vec(Vector([4, 2, 1]))


def test_mat_mat():
    assert Matrix([[1, 0], [0, 1]]).mul_mat(Matrix([[1, 0], [0, 1]])) == Matrix(
        [[1, 0], [0, 1]]
    )
    assert Matrix([[1, 0], [0, 1]]).mul_mat(Matrix([[2, 1], [4, 2]])) == Matrix(
        [[2, 1], [4, 2]]
    )
    assert Matrix([[3, -5], [6, 8]]).mul_mat(Matrix([[2, 1], [4, 2]])) == Matrix(
        [[-14, -7], [44, 22]]
    )
    with pytest.raises(Exception):
        Matrix([[1, 2], [3, 4]]).mul_mat(Matrix([[1, 0], [0, 1], [1, 0]]))
