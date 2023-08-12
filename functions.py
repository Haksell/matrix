from operator import mul
from classes import Vector


def linear_combination(vecs, coefs):
    assert vecs
    assert len(vecs) == len(coefs)
    size = len(vecs[0])
    assert all(len(x) == size for x in vecs)
    return sum(map(mul, vecs, coefs), Vector([0] * size))
