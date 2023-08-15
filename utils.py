def is_close(a, b, eps=1e-6):
    return abs(a - b) <= eps


def clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x
