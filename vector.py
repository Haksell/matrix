import numbers


class Vector:
    def __init__(self, data):
        assert type(data) == list
        assert all(isinstance(x, numbers.Number) for x in data)
        self.__data = data.copy()

    def __iter__(self):
        yield from self.__data

    def __len__(self):
        return len(self.__data)

    def __repr__(self):
        return f"Vector({self.__data})"
