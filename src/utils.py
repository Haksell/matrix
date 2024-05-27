from math import isqrt


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
