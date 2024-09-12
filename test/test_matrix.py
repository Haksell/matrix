from fractions import Fraction
import pytest
from src.utils import is_close
from src import Matrix, Vector


def test_init():
    assert Matrix(Vector([1, 2, 3])) == Matrix([[1], [2], [3]])
    with pytest.raises(Exception):
        Matrix([])
    with pytest.raises(Exception):
        Matrix([[], [], []])


def test_getitem():
    m = Matrix([[1, 2, 3], [4, 5, 6]])
    assert m[0][0] == m[0, 0] == 1
    assert m[0][1] == m[0, 1] == 2
    assert m[0][2] == m[0, 2] == 3
    assert m[1][0] == m[1, 0] == 4
    assert m[1][1] == m[1, 1] == 5
    assert m[1][2] == m[1, 2] == 6
    with pytest.raises(Exception):
        m[2][0]
    with pytest.raises(Exception):
        m[1][3]
    with pytest.raises(Exception):
        m[-1]
    with pytest.raises(Exception):
        m[4]
    with pytest.raises(Exception):
        m[0, 0, 0]
    with pytest.raises(Exception):
        m[0.0]


def test_setitem():
    m = Matrix.zero(2, 3)
    m[0][0] = 42
    m[1] = Vector([1, 2, 3])
    m[1][2] = 27
    assert m == Matrix([[42, 0, 0], [1, 2, 27]])
    with pytest.raises(Exception):
        m[2][0] = 0
    with pytest.raises(Exception):
        m[1][3] = 0
    with pytest.raises(Exception):
        m[-1] = Vector([1, 2, 3])
    with pytest.raises(Exception):
        m[4] = Vector([1, 2, 3])
    with pytest.raises(Exception):
        m[0, 0, 0] = 0
    with pytest.raises(Exception):
        m[0.0] = Vector([1, 2, 3])
    with pytest.raises(Exception):
        m[0] = Vector([1, 2])
    with pytest.raises(Exception):
        m[0] = 42
    with pytest.raises(Exception):
        m[0][0] = Vector([1, 2, 3])


def test_neg():
    assert -Matrix.identity(3) == Matrix([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])
    assert -Matrix([[1, 2], [3.14, 5j]]) == Matrix([[-1, -2], [-3.14, -5j]])


def test_scale():
    assert Matrix([[1, 2], [3 + 4j, 5]]) * 0.5 == Matrix([[0.5, 1.0], [1.5 + 2j, 2.5]])
    with pytest.raises(Exception):
        Matrix.identity(3) * Matrix.zero(3)


def test_add():
    assert Matrix.identity(3) + 3.25 * Matrix.one(3) == Matrix(
        [
            [4.25, 3.25, 3.25],
            [3.25, 4.25, 3.25],
            [3.25, 3.25, 4.25],
        ]
    )
    with pytest.raises(Exception):
        Matrix.identity(2) + Matrix.zero(3)


def test_sub():
    assert Matrix.identity(3) - 3.25 * Matrix.one(3) == Matrix(
        [
            [-2.25, -3.25, -3.25],
            [-3.25, -2.25, -3.25],
            [-3.25, -3.25, -2.25],
        ]
    )
    with pytest.raises(Exception):
        Matrix.identity(2) - 42


def test_trace():
    assert Matrix([[1, 0], [0, 1]]).trace() == 2
    assert Matrix([[2, -5, 0], [4, 3, 7], [-2, 3, 4]]).trace() == 9
    assert Matrix([[-2, -8, 4], [1, -23, 4], [0, 6, 4]]).trace() == -21
    assert Matrix([[-2, -8, 4], [1, -23, 4], [0, 6, 4j]]).trace() == -25 + 4j


def test_conjugate():
    assert Matrix([[1, 0], [0, 1]]).conjugate() == Matrix([[1, 0], [0, 1]])
    assert Matrix([[1j, 0], [0, 1j]]).conjugate() == Matrix([[-1j, 0], [0, -1j]])
    assert Matrix([[1j, 2], [3, 4j], [5j, 6 + 7j]]).conjugate() == Matrix(
        [[-1j, 2], [3, -4j], [-5j, 6 - 7j]]
    )


def test_transpose():
    assert Matrix([[1, 0], [0, 1]]).transpose() == Matrix([[1, 0], [0, 1]])
    assert Matrix([[1, 2], [3, 4]]).transpose() == Matrix([[1, 3], [2, 4]])
    assert Matrix([[1j, 2j, 3j]]).transpose() == Matrix([[1j], [2j], [3j]])


def test_conjugate_transpose():
    assert Matrix([[1, 0], [0, 1]]).conjugate_transpose() == Matrix([[1, 0], [0, 1]])
    assert Matrix([[1, 2], [3, 4]]).conjugate_transpose() == Matrix([[1, 3], [2, 4]])
    assert Matrix([[1j, 2j, 3j]]).conjugate_transpose() == Matrix([[-1j], [-2j], [-3j]])
    assert Matrix([[1j, 0], [0, 1j]]).conjugate_transpose() == Matrix(
        [[-1j, 0], [0, -1j]]
    )
    assert Matrix([[1j, 2], [3, 4j], [5j, 6 + 7j]]).conjugate_transpose() == Matrix(
        [[-1j, 3, -5j], [2, -4j, 6 - 7j]]
    )


def test_row_echelon():
    assert Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]).row_echelon() == Matrix(
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    )
    assert Matrix([[1, 2], [3, 4]]).row_echelon() == Matrix([[1, 0], [0, 1]])
    assert Matrix([[1, 2], [2, 4]]).row_echelon() == Matrix([[1, 2], [0, 0]])
    assert (
        Matrix([[8, 5, -2, 4, 28], [4, 2.5, 20, 4, -4], [8, 5, 1, 4, 17]])
        .row_echelon()
        .is_close(
            Matrix(
                [
                    [1, 0.625, 0, 0, Fraction(-73, 6)],
                    [0, 0, 1, 0, Fraction(-11, 3)],
                    [0, 0, 0, 1, 29.5],
                ]
            )
        )
    )


def test_determinant():
    # TODO test complex
    assert Matrix([[1, -1], [-1, 1]]).determinant() == 0
    assert Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]]).determinant() == 8
    assert Matrix([[2, 0, 0], [0, 0, 2], [0, 2, 0]]).determinant() == -8
    assert Matrix([[0, 2, 0], [2, 0, 0], [0, 0, 2]]).determinant() == -8
    assert Matrix([[0, 2, 0], [0, 0, 2], [2, 0, 0]]).determinant() == 8
    assert Matrix([[0, 0, 2], [2, 0, 0], [0, 2, 0]]).determinant() == 8
    assert Matrix([[0, 0, 2], [0, 2, 0], [2, 0, 0]]).determinant() == -8
    assert is_close(Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]]).determinant(), -174)
    assert is_close(
        Matrix(
            [
                [8, 5, -2, 4],
                [4, 2.5, 20, 4],
                [8, 5, 1, 4],
                [28, -4, 17, 1],
            ]
        ).determinant(),
        1032,
    )
    with pytest.raises(Exception):
        Matrix([[0, 0, 2], [0, 2, 0]]).determinant()


def test_identity():
    assert Matrix.identity(1) == Matrix([[1]])
    assert Matrix.identity(2) == Matrix([[1, 0], [0, 1]])
    assert Matrix.identity(3) == Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert Matrix.identity(4) == Matrix(
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    )
    with pytest.raises(Exception):
        Matrix.identity(-1)
    with pytest.raises(Exception):
        Matrix.identity(0)
    with pytest.raises(Exception):
        Matrix.identity(3.14)


def test_zero():
    assert Matrix.zero(1) == Matrix([[0]])
    assert Matrix.zero(2) == Matrix([[0, 0], [0, 0]])
    assert Matrix.zero(3) == Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    assert Matrix.zero(4) == Matrix(
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    )
    assert Matrix.zero(2, 3) == Matrix([[0, 0, 0], [0, 0, 0]])
    assert Matrix.zero(3, 2) == Matrix([[0, 0], [0, 0], [0, 0]])
    with pytest.raises(Exception):
        Matrix.zero(-1)
    with pytest.raises(Exception):
        Matrix.zero(0)
    with pytest.raises(Exception):
        Matrix.zero(3.14)


def test_one():
    assert Matrix.one(1) == Matrix([[1]])
    assert Matrix.one(2) == Matrix([[1, 1], [1, 1]])
    assert Matrix.one(3) == Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    assert Matrix.one(4) == Matrix(
        [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    )
    assert Matrix.one(2, 3) == Matrix([[1, 1, 1], [1, 1, 1]])
    assert Matrix.one(3, 2) == Matrix([[1, 1], [1, 1], [1, 1]])
    with pytest.raises(Exception):
        Matrix.one(-1)
    with pytest.raises(Exception):
        Matrix.one(0)
    with pytest.raises(Exception):
        Matrix.one(3.14)


def test_augment():
    with pytest.raises(Exception):
        Matrix([[1, 2], [3, 4], [5, 6]]).augment()
    assert Matrix([[1, 0], [0, 1]]).augment() == Matrix([[1, 0, 1, 0], [0, 1, 0, 1]])
    assert Matrix([[7, 7], [7, 7]]).augment() == Matrix([[7, 7, 1, 0], [7, 7, 0, 1]])
    assert Matrix([[7, 7, 7], [7, 7, 7], [7, 7, 7]]).augment() == Matrix(
        [[7, 7, 7, 1, 0, 0], [7, 7, 7, 0, 1, 0], [7, 7, 7, 0, 0, 1]]
    )


def test_inverse():
    # TODO test complex
    with pytest.raises(Exception):
        Matrix([[1, 2], [3, 4], [5, 6]]).inverse()
    with pytest.raises(Exception):
        Matrix([[1, 2, 3], [4, 5, 6], [5, 7, 9]]).inverse()
    assert Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]).inverse() == Matrix(
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    )
    assert Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]]).inverse() == Matrix(
        [[0.5, 0, 0], [0, 0.5, 0], [0, 0, 0.5]]
    )
    assert Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]]).inverse() == Matrix(
        [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
    )
    assert (
        Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]])
        .inverse()
        .is_close(
            Matrix(
                [
                    [0.649425287, 0.097701149, -0.655172414],
                    [-0.781609195, -0.126436782, 0.965517241],
                    [0.143678161, 0.074712644, -0.206896552],
                ]
            )
        )
    )


def test_rank():
    assert Matrix.identity(5).rank() == 5
    assert Matrix.zero(5).rank() == 0
    assert Matrix.one(5).rank() == 1
    assert Matrix([[1, 2, 0, 0], [2, 4, 0, 0], [-1, 2, 1, 1]]).rank() == 2
    assert Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1], [21, 18, 7]]).rank() == 3
