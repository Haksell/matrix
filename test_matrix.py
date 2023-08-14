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
