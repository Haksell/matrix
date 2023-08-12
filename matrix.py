import numbers


class Matrix:
    def __init__(self, values):
        assert type(values) == list
        assert all(type(x) == list for x in values)
        assert all(isinstance(y, numbers.Number) for x in values for y in x)
        assert all(len(x) == len(values[0]) for x in values)
        self.values = values.copy()

    @property
    def shape(self):
        return (len(self.values), len(self.values[0]) if self.values else 0)

    def __len__(self):
        return len(self.values)
