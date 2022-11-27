from pprint import pprint


class FloatValue:
    @classmethod
    def verify_coord(cls, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_coord(value)
        instance.__dict__[self.name] = value


class Cell:
    value = FloatValue()

    def __init__(self, i=float(0)):
        self.value = i


class TableSheet:

    def __init__(self, N, M):
        self.cells = [[Cell() for _ in range(M)] for _ in range(N)]


    @staticmethod
    def iterat(N, M):
        for i in range(1, (N * M) + 1):
            yield float(i)

N = 3
M = 5
table = TableSheet(M, N)
gen_list = TableSheet.iterat(M,N)
for n in range(M):
    for m in range(N):
        table.cells[n][m].value = next(gen_list)

assert isinstance(table, TableSheet)
assert len(table.cells) == 5 and len(table.cells[0]) == 3

assert type(table.cells) == list

res = [int(x.value) for row in table.cells for x in row]
assert res == list(range(1, 16))

table.cells[0][0].value = 1.0
x = table.cells[1][0].value

try:
    table.cells[0][0].value = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"
