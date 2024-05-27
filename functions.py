from src.classes import Vector


def linear_combination(vecs, coefs):
    assert vecs
    assert len(vecs) == len(coefs)
    size = len(vecs[0])
    assert all(len(x) == size for x in vecs)
    return sum(map(Vector.__mul__, vecs, coefs), Vector([0] * size))


def lerp(u, v, t):
    assert type(u) is type(v)
    assert 0 <= t <= 1  # the subject is not clear on this point
    return u * (1 - t) + v * t
