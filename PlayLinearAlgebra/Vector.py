import math


class Vector:

    def __init__(self, lst):
        self._values = list(lst)  # private variable

    @classmethod
    def zero(cls, dim):
        return cls([0] * dim)

    def dot(self, another):
        assert len(self) == len(another), "Error in dot product. Length of vectors must be same."

        return sum(a * b for a, b in zip(self, another))

    def norm(self):
        return math.sqrt(sum(e ** 2 for e in self))

    def projection_coordinate(self, another):
        return (self.dot(another)/another.norm()) * another.normalize()



    def normalize(self):
        if self.norm() < 1e-8:
            raise ZeroDivisionError("Normalize error! Norm is error")
        return Vector(self._values) / self.norm()

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def __repr__(self):
        return "Vector({})".format(self._values)

    # 系统调用

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))

    # print的时候调用

    def __mul__(self, k):
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        return self * k

    # 直接使用上面的mul方法

    def __truediv__(self, k):
        return (1 / k) * self

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    # 重载'+'和'-'

    def __add__(self, other):
        assert len(self) == len(other), "Error in adding. Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, other)])

    # 重载 '+'

    def __sub__(self, other):
        assert len(self) == len(other), "Error in subtracting. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, other)])

    def __iter__(self):
        return self._values.__iter__()
