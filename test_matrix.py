# TODO test repr
# TODO test_init_vector
# TODO test complex multiplication

from classes import Matrix, Vector


def test_mat_vec():
    assert Matrix([[1, 0], [0, 1]]).mul_vec(Vector([4, 2])) == Vector([4, 2])
    assert Matrix([[2, 0], [0, 2]]).mul_vec(Vector([4, 2])) == Vector([8, 4])
    assert Matrix([[2, -2], [-2, 2]]).mul_vec(Vector([4, 2])) == Vector([4, -4])


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
