# TODO test repr/str
# TODO test_init_matrix
# TODO test row and column vectors

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
