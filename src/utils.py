from math import isqrt
import src.vector as V


def linear_combination(vecs, coefs):
    assert vecs
    assert len(vecs) == len(coefs)
    size = len(vecs[0])
    assert all(len(x) == size for x in vecs)
    return sum(map(V.Vector.__mul__, vecs, coefs), V.Vector([0] * size))


def lerp(u, v, t):
    assert type(u) is type(v)
    assert 0 <= t <= 1  # the subject is not clear on this point
    return u * (1 - t) + v * t


def is_close(a, b, eps=1e-6):
    return abs(a - b) <= eps


def clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    return all(n % i != 0 and n % (i + 2) != 0 for i in range(5, isqrt(n) + 1, 6))
