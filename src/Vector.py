from math import sqrt
from numbers import Number
from operator import eq
from utils import clamp, is_close
import src.Matrix as M


class Vector:
    def __init__(self, data):
        if type(data) is M.Matrix:
            if data.height == 1:
                self.__data = list(data[0])
            elif data.width == 1:
                self.__data = [x[0] for x in data]
            else:
                raise ValueError(
                    "Matrix must be a row or column vector, not {data.height}x{data.width}"
                )
        else:
            try:
                self.__data = list(data)
                assert len(self.__data) > 0
                assert all(isinstance(x, Number) for x in self.__data)
            except TypeError:
                raise TypeError(
                    f"{self.__class__.__name__} can't be constructed from type {type(data).__name__}"
                )

    def __eq__(self, other):
        return (
            type(self) is type(other)
            and len(self) == len(other)
            and all(map(eq, self, other))
        )

    def is_close(self, other):
        return len(self) == len(other) and all(map(is_close, self, other))

    def __getitem__(self, idx):
        return self.__data[idx]

    def __setitem__(self, idx, item):
        assert 0 <= idx < len(self)
        assert isinstance(item, Number)
        self.__data[idx] = item

    def __iter__(self):
        yield from self.__data

    def __len__(self):
        return len(self.__data)

    def __repr__(self):
        return f"Vector({self.__data})"

    def __add__(self, other):
        assert len(self) == len(other)
        return Vector([x + y for x, y in zip(self, other)])

    def __iadd__(self, other):
        assert len(self) == len(other)
        for i, x in enumerate(other):
            self.__data[i] += x
        return self

    def __sub__(self, other):
        assert len(self) == len(other)
        return Vector([x - y for x, y in zip(self, other)])

    def __isub__(self, other):
        assert len(self) == len(other)
        for i, x in enumerate(other):
            self.__data[i] -= x
        return self

    def __mul__(self, x):
        return Vector([x * y for y in self])

    __rmul__ = __mul__

    def __imul__(self, x):
        for i in range(len(self)):
            self.__data[i] *= x
        return self

    def dot(self, other):
        assert len(self) == len(other)
        return sum(x * y.conjugate() for x, y in zip(self, other)).real

    def __matmul__(self, other):
        if type(other) is Vector:
            return self.dot(other)
        elif type(other) is M.Matrix:
            assert len(self) == other.height
            return Vector([self.dot(x) for x in other.transpose()])
        else:
            raise TypeError(
                f"{self.__class__.__name__} can't be multiplied with type {type(other).__name__}"
            )

    def norm_1(self):
        return sum(map(abs, self))

    def norm(self):
        return sqrt(self.dot(self))

    def norm_inf(self):
        return max(map(abs, self))

    def angle_cos(self, other):
        assert len(self) == len(other)
        sn = self.norm()
        on = other.norm()
        assert sn and on, "can't compute angle with zero vectors"
        c = (self @ other).real / (sn * on)
        return clamp(c, -1, 1)

    def cross(self, other):
        assert len(self) == len(other) == 3
        return Vector(
            [
                self[1] * other[2] - self[2] * other[1],
                self[2] * other[0] - self[0] * other[2],
                self[0] * other[1] - self[1] * other[0],
            ]
        )

    def conjugate(self):
        return Vector([x.conjugate() for x in self])
