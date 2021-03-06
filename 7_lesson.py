import copy
from abc import ABC, abstractmethod


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for line in self.matrix:
            for elem in line:
                result += f'{elem}\t'
            result +='\n'
        return result

    def __add__(self, second):
        result = copy.deepcopy(self.matrix)
        for i, line in enumerate(result):
            for j, _ in enumerate(line):
                result[i][j] += second.matrix[i][j]
        return Matrix(result)


a = Matrix([[233, 1898, 123], [2, 43, 32], [9384, 3, 399]])
b = Matrix([[10, 20, 30], [10, 20, 30], [10, 20, 30]])

print(a)
print(b)
print(a + b)


class ClothesStructure(ABC):

    @abstractmethod
    def tissue_consumption(self):
        ...


class Clothes(ClothesStructure):
    def __init__(self, name, cl_type, param):
        self.name = name
        self.type = cl_type
        self.param = param

    @property
    def tissue_consumption(self):
        if self.type == 'пальто':
            return self.param * 6.5 + 0.5

        return self.param * 2 + 0.3


coat = Clothes('', 'пальто', 30)
costume = Clothes('', 'костюм', 190)
print(coat.tissue_consumption)
print(costume.tissue_consumption)


class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        if not isinstance(other, Cell): raise Exception
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if not isinstance(other, Cell): raise Exception
        if self.quantity - other.quantity < 0: return 'impossible'
        return Cell(self.quantity - other.quantity)

    def __mul__(self, other):
        if not isinstance(other, Cell): raise Exception
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        if not isinstance(other, Cell): raise Exception
        return Cell(int(self.quantity / other.quantity))

    def __str__(self):
        return f'Клеточек {self.quantity}'

    @staticmethod
    def make_order(cell, cells_number):
        if not isinstance(cell, Cell): raise Exception
        return ('*' * cells_number + '\n') * (cell.quantity // cells_number) + '*' * (cell.quantity % cells_number)



first = Cell(22)
second = Cell(33)
try:
    print(first + second)
    print(first - second)
    print(first * second)
    print(first / second)
    print(Cell.make_order(second, 14))
except:
    print('Sorry')
