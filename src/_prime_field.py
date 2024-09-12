from functools import wraps
import src.utils as U


class PrimeField:
    @staticmethod
    def __validate_prime_field_args(method):
        @wraps(method)
        def wrapper(self, other):
            assert isinstance(other, self.__class__)
            assert self.__p == other.p
            return method(self, other)

        return wrapper

    def __init__(self, n, p):
        assert isinstance(p, int)
        assert U.is_prime(p)
        assert isinstance(n, int)
        assert 0 <= n < p
        self.__n = n
        self.__p = p
        self.__inv = None

    def __repr__(self):
        return f"PrimeField({self.__n}, {self.__p})"

    @property
    def n(self):
        return self.__n

    @property
    def p(self):
        return self.__p

    @property
    def inv(self):
        if self.__inv is None:
            if self.__n == 0:
                raise ZeroDivisionError(
                    "0 does not have a modular inverse in a prime field"
                )
            self.__inv = pow(self.__n, -1, self.__p)
        return self.__inv

    def __neg__(self):
        return PrimeField(0 if self.__n == 0 else self.__p - self.__n, self.__p)

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
    def __floordiv__(self, other):
        return PrimeField(self.__n * other.inv % self.__p, self.__p)

    @__validate_prime_field_args
    def __ifloordiv__(self, other):
        self.__n = self.__n * other.inv % self.__p
        return self
