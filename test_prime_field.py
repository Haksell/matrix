import math
import pytest
from prime_field import PrimeField


def test_init():
    with pytest.raises(AssertionError):
        PrimeField(12, 7)
    with pytest.raises(AssertionError):
        PrimeField(3, 6)
    with pytest.raises(AssertionError):
        PrimeField(math.pi, 7)
    with pytest.raises(AssertionError):
        PrimeField(2, math.pi)


def test_cmp():
    assert PrimeField(3, 7) == PrimeField(3, 7)
    assert not (PrimeField(3, 7) != PrimeField(3, 7))
    assert not (PrimeField(3, 7) < PrimeField(3, 7))
    assert PrimeField(3, 7) <= PrimeField(3, 7)
    assert not (PrimeField(3, 7) > PrimeField(3, 7))
    assert PrimeField(3, 7) >= PrimeField(3, 7)
    assert not (PrimeField(3, 7) == PrimeField(5, 7))
    assert PrimeField(3, 7) != PrimeField(5, 7)
    assert PrimeField(3, 7) < PrimeField(5, 7)
    assert PrimeField(3, 7) <= PrimeField(5, 7)
    assert not (PrimeField(3, 7) > PrimeField(5, 7))
    assert not (PrimeField(3, 7) >= PrimeField(5, 7))
    assert not (PrimeField(5, 7) == PrimeField(3, 7))
    assert PrimeField(5, 7) != PrimeField(3, 7)
    assert not (PrimeField(5, 7) < PrimeField(3, 7))
    assert not (PrimeField(5, 7) <= PrimeField(3, 7))
    assert PrimeField(5, 7) > PrimeField(3, 7)
    assert PrimeField(5, 7) >= PrimeField(3, 7)
    with pytest.raises(AssertionError):
        assert PrimeField(3, 7) != PrimeField(5, 11)


def test_neg():
    assert -PrimeField(0, 7) == PrimeField(0, 7)
    assert -PrimeField(1, 7) == PrimeField(6, 7)
    assert -PrimeField(2, 7) == PrimeField(5, 7)
    assert -PrimeField(3, 7) == PrimeField(4, 7)
    assert -PrimeField(4, 7) == PrimeField(3, 7)
    assert -PrimeField(5, 7) == PrimeField(2, 7)
    assert -PrimeField(6, 7) == PrimeField(1, 7)


def test_add():
    assert PrimeField(2, 7) + PrimeField(0, 7) == PrimeField(2, 7)
    assert PrimeField(2, 7) + PrimeField(2, 7) == PrimeField(4, 7)
    assert PrimeField(2, 7) + PrimeField(4, 7) == PrimeField(6, 7)
    assert PrimeField(2, 7) + PrimeField(6, 7) == PrimeField(1, 7)
    pf = PrimeField(2, 7)
    pf += PrimeField(3, 7)
    assert pf == PrimeField(5, 7)


def test_sub():
    assert PrimeField(2, 7) - PrimeField(0, 7) == PrimeField(2, 7)
    assert PrimeField(2, 7) - PrimeField(2, 7) == PrimeField(0, 7)
    assert PrimeField(2, 7) - PrimeField(4, 7) == PrimeField(5, 7)
    assert PrimeField(2, 7) - PrimeField(6, 7) == PrimeField(3, 7)
    pf = PrimeField(2, 7)
    pf -= PrimeField(3, 7)
    assert pf == PrimeField(6, 7)


def test_pow():
    pass
