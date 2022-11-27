class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        self.__prev = prev

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if isinstance(data, StackObj):
            self.__data = data


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top == None:
            self.top = obj
            self.tail = obj
        else:
            obj.prev = self.tail
            self.tail.next = obj
            self.tail = obj


    def pop(self):
        if self.top == None:
            return self.top
        if self.top.next == None and self.top.prev == None:
            self.top = None
            obj = self.tail
            return obj
        obj = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return obj

    def get_data(self):
        if self.top == None:
            return []
        respons_obj = []
        next_var = self.top
        while next_var != None:
            respons_obj.append(next_var.data)
            next_var = next_var.next
        return respons_obj


s = Stack()
top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()

res = s.get_data()
assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

h = s.top
while h:
    res = h.data
    h = h.next

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

n = 0
h = s.top
while h:
    h = h.next
    n += 1

assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"

s = Stack()
top = StackObj("name_1")
s.push(top)
obj = s.pop()
assert obj == top, "метод pop() должен возвращать удаляемый объект"
