from copy import deepcopy
import numbers


class Vector:
    def __init__(self, data):
        if type(data) == list:
            assert all(isinstance(x, numbers.Number) for x in data)
            self.__data = data.copy()
        elif type(data) == Matrix:
            if data.height == 1:
                self.__data = data[0]
            elif data.width == 1:
                self.__data = [x[0] for x in data]
            else:
                raise TypeError(
                    f"Matrix must be a row or column vector, not {data.shape}"
                )
        else:
            raise TypeError(
                f"{self.__class__.__name__} can't be constructed from a {type(data).__name__}"
            )
        assert type(data) == list
        assert all(isinstance(x, numbers.Number) for x in data)
        self.__data = data.copy()

    def __iter__(self):
        yield from self.__data

    def __len__(self):
        return len(self.__data)

    def __repr__(self):
        return f"Vector({self.__data})"


class Matrix:
    def __init__(self, data):
        if type(data) == list:
            assert all(type(x) == list for x in data)
            assert all(isinstance(y, numbers.Number) for x in data for y in x)
            assert len(data) == 0 or all(len(x) == len(data[0]) for x in data)
            self.__height = len(data)
            self.__width = len(data[0]) if self.__height else 0
            self.__data = deepcopy(data)
        elif type(data) == Vector:
            self.__height = len(data)
            self.__width = 1
            self.__data = [Vector(x) for x in data]
        else:
            raise TypeError(
                f"{self.__class__.__name__} can't be constructed from a {type(data).__name__}"
            )

    def __getitem__(self, idx):
        assert 0 <= idx < self.__height
        return self.__data[idx]

    def __iter__(self):
        yield from self.__data

    def __len__(self):
        return self.__height

    def __repr__(self):
        return f"Matrix({self.__data})"

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
