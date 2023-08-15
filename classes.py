from copy import deepcopy
from math import sqrt
from numbers import Number
from operator import eq
from utils import clamp, is_close


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
        return (
            type(self) == type(other)
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
    # TODO Moore-Penrose pseudoinverse
    # TODO Singular Value Decomposition
    # TODO eigenstuff
    class SingularException(Exception):
        def __init__(self, matrix):
            super().__init__(f"{matrix} is singular")

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

    @staticmethod
    def identity(n):
        assert type(n) == int
        assert n >= 1
        return Matrix([[1 if x == y else 0 for x in range(n)] for y in range(n)])

    @staticmethod
    def zero(h, w=None):
        if w is None:
            w = h
        assert type(h) == int
        assert h >= 1
        return Matrix([[0] * w for y in range(h)])

    @staticmethod
    def one(h, w=None):
        if w is None:
            w = h
        assert type(h) == int
        assert h >= 1
        return Matrix([[1] * w for y in range(h)])

    def __eq__(self, other):
        return (
            type(self) == type(other)
            and self.shape == other.shape
            and all(map(Vector.__eq__, self, other))
        )

    def is_close(self, other):
        return self.shape == other.shape and all(map(Vector.is_close, self, other))

    def __getitem__(self, idx):
        return self.__data[idx]

    def __setitem__(self, idx, item):
        assert 0 <= idx < len(self)
        assert isinstance(item, Vector)
        assert len(item) == self.__width
        self.__data[idx] = item

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
        return self.conjugate().transpose()

    def rref_det(self):
        res = deepcopy(self.__data)
        determinant = 1
        y = 0
        for x in range(self.__width):
            y_swap = next(
                (y2 for y2 in range(y, self.__height) if res[y2][x] != 0),
                None,
            )
            if y_swap is None:
                determinant = 0
                continue
            elif y_swap != y:
                determinant = -determinant
                res[y], res[y_swap] = res[y_swap], res[y]
            determinant *= res[y][x]
            res[y] *= 1 / res[y][x]
            for y2 in range(self.__height):
                if y != y2 and res[y2][x] != 0:
                    res[y2] -= res[y2][x] * res[y]
            y += 1
            if y == self.__height:
                break
        res = Matrix(res)
        return (res, determinant)

    def row_echelon(self):
        return self.rref_det()[0]

    def determinant(self):
        assert self.is_square()
        return self.rref_det()[1]

    def augment(self):
        assert self.is_square()
        return Matrix(
            [
                list(v1) + list(v2)
                for v1, v2 in zip(self, Matrix.identity(self.__height))
            ]
        )

    def inverse(self):
        assert self.is_square()
        augmented = self.augment()
        for y in range(self.__height):
            y_swap = next(
                (y2 for y2 in range(y, self.__height) if augmented[y2][y] != 0),
                None,
            )
            if y_swap is None:
                raise Matrix.SingularException(self)
            elif y_swap != y:
                tmp = augmented[y]
                augmented[y] = augmented[y_swap]
                augmented[y_swap] = tmp
            augmented[y] *= 1 / augmented[y][y]
            for y2 in range(self.__height):
                if y != y2 and augmented[y2][y] != 0:
                    augmented[y2] -= augmented[y2][y] * augmented[y]
        return Matrix([list(v)[self.__width :] for v in augmented])

    def rank(self):
        return sum(any(x != 0 for x in row) for row in self.row_echelon())
