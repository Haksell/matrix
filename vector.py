# TODO add __iter__ and other magic methods

import numbers


class Vector:
    def __init__(self, values):
        assert type(values) == list
        assert all(isinstance(x, numbers.Number) for x in values)
        self.values = values.copy()

    def __len__(self):
        return len(self.values)
