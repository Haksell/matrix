# TODO test repr/str
# TODO test_init_matrix
# TODO test mul/rmul
# TODO test row and column vectors
# TODO test norm of complex numbers

from math import pi
import pytest
from classes import Vector


def test_init():
    Vector([])
    Vector([42])
    assert Vector([42, pi, 1j]) == Vector((42, pi, 1j))
    with pytest.raises(Exception):
        Vector()
    with pytest.raises(Exception):
        Vector(42)


def test_len():
    assert len(Vector([])) == 0
    assert len(Vector([42])) == 1
    assert len(Vector([42, pi, 1j])) == 3


def test_matmul():
    assert Vector([1, 2, 3]) @ Vector([1, 2, 3]) == 14
    assert Vector([1j, 2j, 3j]) @ Vector([1j, 2j, 3]) == -5 + 9j
    assert Vector([1, 0]) @ Vector([0, 1]) == 0
    with pytest.raises(Exception):
        Vector([1, 2]) @ Vector([1, 2, 3])


def test_norm():
    norms = lambda v: (v.norm_1(), v.norm(), v.norm_inf())
    assert norms(Vector([0, 0, 0])) == (0, 0, 0)
    assert norms(Vector([1, 2, 2])) == (5, 3, 2)
    assert norms(Vector([-4, 3])) == (7, 5, 4)
