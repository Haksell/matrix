import numbers


class Vector:
    def __init__(self, values):
        assert type(values) == list
        assert all(isinstance(x, numbers.Number) for x in values)
        self.__values = values.copy()

    def __len__(self):
        return len(self.__values)

    def __repr__(self):
        return f"Vector({self.__values})"
