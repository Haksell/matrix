# TODO matrix transpose

from copy import deepcopy
import numbers
from vector import Vector


class Matrix:
    def __init__(self, data):
        if type(data) == list:
            assert all(type(x) == list for x in data)
            assert all(isinstance(y, numbers.Number) for x in data for y in x)
            assert all(len(x) == len(data[0]) for x in data)
            self.__height = len(data)
            self.__width = len(data[0]) if self.__height else 0
            self.__data = deepcopy(data)
        elif type(data) == Vector:
            self.__height = len(data)
            self.__width = 1
            self.__data = [[x] for x in data]
        else:
            raise TypeError(
                f"{self.__class__.__name__} can't be constructed from a {type(data).__name__}"
            )

    def __iter__(self):
        yield from self.__data

    def __len__(self):
        return self.__height

    def __repr__(self):
        return f"Matrix({self.__data})"

    @property
    def shape(self):
        return (self.__height, self.__width)
