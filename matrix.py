from copy import deepcopy
import numbers


class Matrix:
    def __init__(self, values):
        assert type(values) == list
        assert all(type(x) == list for x in values)
        assert all(isinstance(y, numbers.Number) for x in values for y in x)
        assert all(len(x) == len(values[0]) for x in values)
        self.__values = deepcopy(values)
        self.__height = len(self.__values)
        self.__width = len(self.__values[0]) if self.__height else 0

    @property
    def shape(self):
        return (self.__height, self.__width)

    def __len__(self):
        return self.__height

    def __repr__(self):
        return f"Matrix({self.__values})"
