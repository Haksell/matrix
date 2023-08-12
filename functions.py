from classes import Vector


def linear_combination(vecs, coefs):
    assert len(vecs) == len(coefs)
    if len(vecs) == 0:
        return Vector([])
    assert all(len(x) == len(vecs[0]) for x in vecs)
    return sum(
        [vec * coef for vec, coef in zip(vecs, coefs)], Vector([0] * len(vecs[0]))
    )  # TODO why do we need a starting value?
