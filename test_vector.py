from math import pi
import pytest
from vector import Vector


def test_init():
    Vector([])
    Vector([42])
    Vector([42, pi, 1j])
    with pytest.raises(Exception):
        Vector()
    with pytest.raises(Exception):
        Vector(42)
    with pytest.raises(Exception):
        Vector((42, pi, 1j))


def test_len():
    assert len(Vector([])) == 0
    assert len(Vector([42])) == 1
    assert len(Vector([42, pi, 1j])) == 3
