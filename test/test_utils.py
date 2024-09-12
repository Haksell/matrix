import math
import pytest
from projection_matrix import projection_matrix
from src import Matrix, Vector
from src.utils import is_close, is_prime, lerp, linear_combination


def test_linear_combination_valid():
    assert linear_combination([Vector([1, 2, 3])], [1]) == Vector([1, 2, 3])
    assert linear_combination([Vector([1, 2, 3])], [2]) == Vector([2, 4, 6])
    assert linear_combination([Vector([1, 2, 3]), Vector([4, 5, 6])], [7, 8]) == Vector(
        [39, 54, 69]
    )
    assert linear_combination(
        [Vector([1, 2, 3]), Vector([2, 4, 6])], [2, -1]
    ) == Vector([0, 0, 0])
    assert linear_combination(
        [Vector([0, 0]), Vector([1, 1]), Vector([2, 2])], [1, 1, 1]
    ) == Vector([3, 3])
    assert linear_combination(
        [Vector([1, 0, 0]), Vector([0, 1, 0]), Vector([0, 0, 1])], [1, 2, 3]
    ) == Vector([1, 2, 3])
    assert linear_combination(
        [Vector([1, 2, 3j]), Vector([4, 5j, 6])], [7, 8]
    ) == Vector([39, 14 + 40j, 48 + 21j])


def test_linear_combination_invalid():
    with pytest.raises(Exception):
        linear_combination([Vector([1])], [1, 1])
    with pytest.raises(Exception):
        linear_combination([Vector([1]), Vector([1])], [1])
    with pytest.raises(Exception):
        linear_combination([Vector([1]), Vector([1, 1])], [1, 1])
    with pytest.raises(Exception):
        linear_combination([], [])


def test_lerp_scalar():
    assert lerp(0, 1, 0) == 0
    assert lerp(0, 2, 0.5) == 1
    assert lerp(0, 2, 1) == 2
    assert lerp(3 + 4j, 7 + 0j, 0.5) == 5 + 2j


def test_lerp_vector():
    assert lerp(Vector([0, 1]), Vector([1, 0]), 0) == Vector([0, 1])
    assert lerp(Vector([0, 1]), Vector([1, 0]), 0.5) == Vector([0.5, 0.5])
    assert lerp(Vector([0, 1]), Vector([1, 0]), 1) == Vector([1, 0])
    assert lerp(Vector([3, 2 + 3j]), Vector([-1, 4j]), 0.75) == Vector([0, 0.5 + 3.75j])


def test_lerp_matrix():
    assert lerp(Matrix([[0, 1], [2, 3]]), Matrix([[3, 2], [1, 0]]), 0) == Matrix(
        [[0, 1], [2, 3]]
    )
    assert lerp(Matrix([[0, 1], [2, 3]]), Matrix([[3, 2], [1, 0]]), 0.5) == Matrix(
        [[1.5, 1.5], [1.5, 1.5]]
    )
    assert lerp(Matrix([[0, 1], [2, 3]]), Matrix([[3, 2], [1, 0]]), 1) == Matrix(
        [[3, 2], [1, 0]]
    )


def test_lerp_invalid():
    with pytest.raises(Exception):
        lerp(0, 1, -1)
    with pytest.raises(Exception):
        lerp(0, 1, 1.5)
    with pytest.raises(Exception):
        lerp(Vector([1]), Matrix([[1]]), 0.5)


def test_projection_matrix():
    def check_same_matrices(expected, result):
        assert expected.shape == result.shape
        assert all(
            is_close(expected[y][x], result[y][x]) for y in range(4) for x in range(4)
        )

    check_same_matrices(
        projection_matrix(math.radians(90), 16 / 9, 0.1, 100),
        Matrix(
            [
                [0.5625, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, -1.002002, -1],
                [0, 0, -0.1001001, 0],
            ]
        ),
    )
    check_same_matrices(
        projection_matrix(math.radians(80), 1, 0.1, 100),
        Matrix(
            [
                [1.19175359, 0, 0, 0],
                [0, 1.19175359, 0, 0],
                [0, 0, -1.002002, -1],
                [0, 0, -0.1001001, 0],
            ]
        ),
    )
    check_same_matrices(
        projection_matrix(math.radians(80), 1, 0.1, 7),
        Matrix(
            [
                [1.19175359, 0, 0, 0],
                [0, 1.19175359, 0, 0],
                [0, 0, -1.02898551, -1],
                [0, 0, -0.10144928, 0],
            ]
        ),
    )


def test_is_prime():
    assert not is_prime(-1)
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)
    assert not is_prime(8)
    assert not is_prime(9)
    assert not is_prime(10)
    assert is_prime(11)
    assert not is_prime(12)
    assert is_prime(13)
    assert not is_prime(14)
    assert not is_prime(15)
    assert not is_prime(16)
    assert is_prime(17)
    assert not is_prime(18)
    assert is_prime(19)
    assert not is_prime(10)
    assert not is_prime(21)
    assert not is_prime(22)
    assert is_prime(23)
    assert not is_prime(24)
    assert not is_prime(25)
    assert not is_prime(26)
    assert not is_prime(27)
    assert not is_prime(28)
    assert is_prime(29)
