# TODO test repr
# TODO test_init_vector
# TODO test complex multiplication

from classes import Matrix, Vector


def test_mat_vec():
    # TODO test fail
    assert Matrix([[1, 0], [0, 1]]).mul_vec(Vector([4, 2])) == Vector([4, 2])
    assert Matrix([[2, 0], [0, 2]]).mul_vec(Vector([4, 2])) == Vector([8, 4])
    assert Matrix([[2, -2], [-2, 2]]).mul_vec(Vector([4, 2])) == Vector([4, -4])


def test_mat_mat():
    # TODO test fail
    assert Matrix([[1, 0], [0, 1]]).mul_mat(Matrix([[1, 0], [0, 1]])) == Matrix(
        [[1, 0], [0, 1]]
    )
    assert Matrix([[1, 0], [0, 1]]).mul_mat(Matrix([[2, 1], [4, 2]])) == Matrix(
        [[2, 1], [4, 2]]
    )
    assert Matrix([[3, -5], [6, 8]]).mul_mat(Matrix([[2, 1], [4, 2]])) == Matrix(
        [[-14, -7], [44, 22]]
    )


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
                    [1, 0.625, 0, 0, -12.1666667],
                    [0, 0, 1, 0, -3.6666667],
                    [0, 0, 0, 1, 29.5],
                ]
            )
        )
    )


def test_determinant():
    assert Matrix([[1, -1], [-1, 1]]).determinant() == 0
    assert Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]]).determinant() == 8
    assert Matrix([[2, 0, 0], [0, 0, 2], [0, 2, 0]]).determinant() == -8
    assert Matrix([[0, 2, 0], [2, 0, 0], [0, 0, 2]]).determinant() == -8
    assert Matrix([[0, 2, 0], [0, 0, 2], [2, 0, 0]]).determinant() == 8
    assert Matrix([[0, 0, 2], [2, 0, 0], [0, 2, 0]]).determinant() == 8
    assert Matrix([[0, 0, 2], [0, 2, 0], [2, 0, 0]]).determinant() == -8
