from functools import cache, wraps
from math import isqrt

# TODO: inverse
# TODO: division by inverse
# TODO: fix exponentiation


@cache
def _is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    return all(n % i != 0 and n % (i + 2) != 0 for i in range(5, isqrt(n) + 1, 6))


class PrimeField:
    def __init__(self, n, p):
        assert isinstance(p, int)
        assert _is_prime(p)
        assert isinstance(n, int)
        assert 0 <= n < p
        self.__n = n
        self.__p = p

    def __repr__(self):
        return f"PrimeField({self.__n}, {self.__p})"

    @property
    def n(self):
        return self.__n

    @property
    def p(self):
        return self.__p

    def __neg__(self):
        return PrimeField(0 if self.__n == 0 else self.__p - self.__n, self.__p)

    @staticmethod
    def __validate_prime_field_args(method):
        @wraps(method)
        def wrapper(self, other):
            assert isinstance(other, self.__class__)
            assert self.__p == other.p
            return method(self, other)

        return wrapper

    @__validate_prime_field_args
    def __eq__(self, other):
        return self.__n == other.n

    @__validate_prime_field_args
    def __ne__(self, other):
        return self.__n != other.n

    @__validate_prime_field_args
    def __lt__(self, other):
        return self.__n < other.n

    @__validate_prime_field_args
    def __le__(self, other):
        return self.__n <= other.n

    @__validate_prime_field_args
    def __gt__(self, other):
        return self.__n > other.n

    @__validate_prime_field_args
    def __ge__(self, other):
        return self.__n >= other.n

    @__validate_prime_field_args
    def __add__(self, other):
        return PrimeField((self.__n + other.n) % self.__p, self.__p)

    @__validate_prime_field_args
    def __iadd__(self, other):
        self.__n = (self.__n + other.n) % self.__p
        return self

    @__validate_prime_field_args
    def __sub__(self, other):
        return PrimeField((self.__n - other.n) % self.__p, self.__p)

    @__validate_prime_field_args
    def __isub__(self, other):
        self.__n = (self.__n - other.n) % self.__p
        return self

    @__validate_prime_field_args
    def __mul__(self, other):
        return PrimeField(self.__n * other.n % self.__p, self.__p)

    @__validate_prime_field_args
    def __imul__(self, other):
        self.__n = self.__n * other.n % self.__p
        return self

    @__validate_prime_field_args
    def __pow__(self, other):
        self.__n = self.__n * other.n % self.__p
        return self
