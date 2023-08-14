from math import sqrt
from numbers import Number
from operator import eq
from utils import clamp


class Vector:
    def __init__(self, data):
        if type(data) == Matrix:
            if data.height == 1:
                self.__data = list(data[0])
            elif data.width == 1:
                self.__data = [x[0] for x in data]
            else:
                raise ValueError(
                    f"Matrix must be a row or column vector, not {data.height}x{data.width}"
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
        return len(self) == len(other) and all(map(eq, self, other))

    def __getitem__(self, idx):
        return self.__data[idx]

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
        if type(other) == Vector:
            return self.dot(other)
        elif type(other) == Matrix:
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


class Matrix:
    def __init__(self, data):
        if type(data) == list:
            assert all(type(x) == list or type(x) == Vector for x in data)
            assert all(isinstance(y, Number) for x in data for y in x)
            assert len(data) != 0 and len(data[0]) != 0
            assert all(len(x) == len(data[0]) for x in data)
            self.__height = len(data)
            self.__width = len(data[0])
            self.__data = [Vector(x) for x in data]
        elif type(data) == Vector:
            self.__height = len(data)
            self.__width = 1
            self.__data = [Vector([x]) for x in data]
        else:
            raise TypeError(
                f"{self.__class__.__name__} can't be constructed from type {type(data).__name__}"
            )

    def __eq__(self, other):
        return self.shape == other.shape and all(map(Vector.__eq__, self, other))

    def __getitem__(self, idx):
        return self.__data[idx]

    def __iter__(self):
        yield from self.__data

    def __len__(self):
        return self.__height

    def __repr__(self):
        return f"Matrix({list(map(list, self))})"

    def __add__(self, other):
        assert self.shape == other.shape
        return Matrix([x + y for x, y in zip(self, other)])

    def __iadd__(self, other):
        assert self.shape == other.shape
        for i, x in enumerate(other):
            self.__data[i] += x
        return self

    def __sub__(self, other):
        assert self.shape == other.shape
        return Vector([x - y for x, y in zip(self, other)])

    def __isub__(self, other):
        assert self.shape == other.shape
        for i, x in enumerate(other):
            self.__data[i] -= x
        return self

    def __mul__(self, x):
        return Matrix([x * y for y in self])

    __rmul__ = __mul__

    def __imul__(self, x):
        for i in range(len(self)):
            self.__data[i] *= x
        return self

    def mul_vec(self, other):
        assert self.width == len(other)
        return Vector([x.dot(other) for x in self])

    def mul_mat(self, other):
        # TODO test complex multiplication
        # https://mathworld.wolfram.com/ComplexMatrix.html
        assert self.width == other.height
        return Matrix([self.mul_vec(x) for x in other.transpose()]).transpose()

    def __matmul__(self, other):
        if type(other) == Vector:
            return self.mul_vec(other)
        elif type(other) == Matrix:
            return self.mul_mat(other)
        else:
            raise TypeError(
                f"{self.__class__.__name__} can't be multiplied with type {type(other).__name__}"
            )

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def shape(self):
        return (self.__height, self.__width)

    def is_square(self):
        return self.__width == self.__height

    def trace(self):
        assert self.is_square()
        return sum(self[i][i] for i in range(self.__height))

    def conjugate(self):
        return Matrix([x.conjugate() for x in self])

    def transpose(self):
        return Matrix(
            [
                [self.__data[y][x] for y in range(self.__height)]
                for x in range(self.__width)
            ]
        )

    def conjugate_transpose(self):
        return self.transpose().conjugate()
