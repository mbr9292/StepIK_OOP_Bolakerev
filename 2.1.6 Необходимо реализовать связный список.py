class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.id = 0
        self.list_of_available = None

    def add_obj(self, obj):
        if self.id == 0:
            self.head = obj
            self.id += 1
        else:
            self.list_of_available.set_next(obj)
            obj.set_prev(self.list_of_available)
            self.tail = obj
            obj.set_next(None)
            self.id += 1
        self.list_of_available = obj


    def remove_obj(self):
        if self.id == 1:
            self.head = None
            self.tail = None
            self.list_of_available = None
            self.id = 0
        else:
            obj = self.list_of_available.get_prev()
            obj.set_next(None)


    def get_data(self):
        obj = self.head
        respons = []
        i = 0
        while i!=self.id :
                respons.append(obj.get_data())
                obj = obj.get_next()
                i += 1
        return respons


# print(123)
# lst = LinkedList()
# # lst.add_obj(ObjList("данные 4"))
# # lst.add_obj(ObjList("данные 5"))
# # lst.add_obj(ObjList("данные 6"))
# # lst.add_obj(ObjList("данные 7"))
# res = lst.get_data()  # ['данные 1', 'данные 2', 'данные 3']
# print(res)
# lst.remove_obj()
# res = lst.get_data()  # ['данные 1', 'данные 2', 'данные 3']
#
ls = LinkedList()
ls.add_obj(ObjList("данные 1"))
ls.add_obj(ObjList("данные 2"))
ls.add_obj(ObjList("данные 3"))
ls.add_obj(ObjList("данные 34"))
assert ls.get_data() == ['данные 1', 'данные 2', 'данные 3', 'данные 34'], "метод get_data вернул неверные данные"

ls_one = LinkedList()
ls_one.add_obj(ObjList(1))
assert ls_one.get_data() == [1], "метод get_data вернул неверные данные"

h = ls_one.head
n = 0
while h:
    n += 1
    h = h.get_next()

assert n == 1, "неверное число объектов в списке: возможно некорректно работает метод add_obj"
ls_one.remove_obj()
assert ls_one.get_data() == [], "метод get_data вернул неверные данные для пустого списка, возможно, неверно работает метод remove_obj"

ls2 = LinkedList()
assert ls.head != ls2.head, "атрибут head должен принадлежать объекту класса LinkedList, а не самому классу"
assert ls.tail != ls2.tail, "атрибут tail должен принадлежать объекту класса LinkedList, а не самому классу"

h = ls.head
n = 0
while h:
    n += 1
    h = h.get_next()

assert n == 4, "неверное число объектов в списке: возможно некорректно работает метод add_obj"

h = ls.head
n = 0
while h:
    h = h._ObjList__next
    n += 1

assert n == 4, "неверное число объектов в списке: возможно некорректные значения в атрибутах __next"

h = ls.tail
n = 0
while h:
    n += 1
    h = h.get_prev()

assert n == 4, "неверное число объектов в списке: возможно некорректно работает метод add_obj"

h = ls.tail
n = 0
while h:
    h = h._ObjList__prev
    n += 1

assert n == 4, "неверное число объектов в списке: возможно некорректные значения в атрибутах __prev"
