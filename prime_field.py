from functools import cache, wraps
from math import isqrt


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
    def __init__(self, n, prime):
        assert isinstance(prime, int)
        assert _is_prime(prime)
        assert isinstance(n, int)
        assert 0 <= n < prime
        self.n = n
        self.prime = prime

    def __repr__(self):
        return f"PrimeField({self.n}, {self.prime})"

    @staticmethod
    def __validate_prime_field_args(method):
        @wraps(method)
        def wrapper(self, other):
            assert isinstance(other, self.__class__)
            assert self.prime == other.prime
            return method(self, other)

        return wrapper

    @__validate_prime_field_args
    def __eq__(self, other):
        return self.n == other.n

    @__validate_prime_field_args
    def __ne__(self, other):
        return self.n != other.n

    @__validate_prime_field_args
    def __lt__(self, other):
        return self.n < other.n

    @__validate_prime_field_args
    def __le__(self, other):
        return self.n <= other.n

    @__validate_prime_field_args
    def __gt__(self, other):
        return self.n > other.n

    @__validate_prime_field_args
    def __ge__(self, other):
        return self.n >= other.n

    @__validate_prime_field_args
    def __add__(self, other):
        return PrimeField((self.n + other.n) % self.prime, self.prime)

    @__validate_prime_field_args
    def __iadd__(self, other):
        self.n = (self.n + other.n) % self.prime
        return self

    @__validate_prime_field_args
    def __sub__(self, other):
        return PrimeField((self.n - other.n) % self.prime, self.prime)

    @__validate_prime_field_args
    def __isub__(self, other):
        self.n = (self.n - other.n) % self.prime
        return self

    @__validate_prime_field_args
    def __mul__(self, other):
        return PrimeField(self.n * other.n % self.prime, self.prime)

    @__validate_prime_field_args
    def __imul__(self, other):
        self.n = self.n * other.n % self.prime
        return self

    @__validate_prime_field_args
    def __pow__(self, other):
        self.n = self.n * other.n % self.prime
        return self
