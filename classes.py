# add, iadd, sub, isub, mul, imul, rmul
import numbers


class Vector:
    def __init__(self, data):
        if type(data) == Matrix:
            if data.height == 1:
                self.__data = data[0].copy()
            elif data.width == 1:
                self.__data = [x[0] for x in data]
            else:
                raise ValueError(
                    f"Matrix must be a row or column vector, not {data.height}x{data.width}"
                )
        else:
            try:
                data = list(data)
                assert all(isinstance(x, numbers.Number) for x in data)
                self.__data = data.copy()
            except TypeError:
                raise TypeError(
                    f"{self.__class__.__name__} can't be constructed from a {type(data).__name__}"
                )

    def __eq__(self, other):
        return len(self) == len(other) and all(x == y for x, y in zip(self, other))

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

    def __matmul__(self, other):
        assert len(self) == len(other)
        return sum(x * y for x, y in zip(self, other))


class Matrix:
    def __init__(self, data):
        if type(data) == list:
            assert all(type(x) == list or type(x) == Vector for x in data)
            assert all(isinstance(y, numbers.Number) for x in data for y in x)
            assert len(data) == 0 or all(len(x) == len(data[0]) for x in data)
            self.__height = len(data)
            self.__width = len(data[0]) if self.__height else 0
            self.__data = [Vector(x) for x in data]
        elif type(data) == Vector:
            self.__height = len(data)
            self.__width = 1
            self.__data = [Vector([x]) for x in data]
        else:
            raise TypeError(
                f"{self.__class__.__name__} can't be constructed from a {type(data).__name__}"
            )

    def __eq__(self, other):
        return self.shape == other.shape and all(x == y for x, y in zip(self, other))

    def __getitem__(self, idx):
        return self.__data[idx]

    def __iter__(self):
        yield from self.__data

    def __len__(self):
        return self.__height

    def __repr__(self):
        return f"Matrix({self.__data})"

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

    def transpose(self):
        return Matrix(
            [
                [self.__data[y][x] for y in range(self.__height)]
                for x in range(self.__width)
            ]
        )
