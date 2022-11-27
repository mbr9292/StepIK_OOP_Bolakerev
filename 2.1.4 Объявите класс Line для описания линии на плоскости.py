class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__r = (x1, y1, x2, y2)

    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__r = (x1, y1, x2, y2)

    def get_coords(self):
        return self.__r

    def draw(self):
        print(' '.join(str(i) for i in self.__r))


a = Line(1, 2, 3, 4)
s = a.get_coords()
print(s) # (1, 2, 3, 4)
a.draw() # 1 2 3 4
