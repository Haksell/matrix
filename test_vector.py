# TODO test repr/str
# TODO test_init_matrix
# TODO test mul/rmul
# TODO test row and column vectors
# TODO test norms of complex numbers
# TODO test angle_cos of complex numbers
# TODO test_angle_cos with 0 vector

from math import pi
import pytest
from classes import Vector
from utils import is_close


def test_init():
    Vector([42])
    assert Vector([42, pi, 1j]) == Vector((42, pi, 1j))
    with pytest.raises(Exception):
        Vector([])
    with pytest.raises(Exception):
        Vector()
    with pytest.raises(Exception):
        Vector(42)


def test_len():
    assert len(Vector([42])) == 1
    assert len(Vector([42, pi, 1j])) == 3


def test_matmul():
    assert Vector([1, 2, 3]) @ Vector([1, 2, 3]) == 14
    assert Vector([1, 0]) @ Vector([0, 1]) == 0
    with pytest.raises(Exception):
        Vector([1, 2]) @ Vector([1, 2, 3])


def test_norm():
    norms = lambda v: (v.norm_1(), v.norm(), v.norm_inf())
    assert norms(Vector([0, 0, 0])) == (0, 0, 0)
    assert norms(Vector([1, 2, 2])) == (5, 3, 2)
    assert norms(Vector([-4, 3])) == (7, 5, 4)


def test_angle_cos():
    assert is_close(Vector([1, 0]).angle_cos(Vector([1, 0])), 1)
    assert is_close(Vector([1, 0]).angle_cos(Vector([0, 1])), 0)
    assert is_close(Vector([-1, 1]).angle_cos(Vector([1, -1])), -1)
    assert is_close(Vector([1, 2]).angle_cos(Vector([2, 4])), 1)
    assert is_close(Vector([1, 2, 3]).angle_cos(Vector([4, 5, 6])), 0.974631846)
