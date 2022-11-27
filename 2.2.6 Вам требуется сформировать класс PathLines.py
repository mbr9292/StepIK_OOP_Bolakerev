from math import sqrt


class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):

        if len(args) == 0:
            add = LineTo()
            self.__lines = [add]
        else:
            add = LineTo()
            self.__lines = [add]
            for i in args:
                self.__lines.append(i)


    def get_path(self):
        return self.__lines

    def get_length(self):
        if len(self.__lines)<2:
            return 0
        else:
            L=0
            for i in range(len(self.__lines)-1):
                x1 = self.__lines[i+1].x
                x0 = self.__lines[i].x
                y1 = self.__lines[i+1].y
                y0 = self.__lines[i].y
                L+= sqrt(((x1 - x0)**2) + ((y1 - y0) ** 2))
            return L


    def add_line(self, line):
        self.__lines.append(line)


p = PathLines(LineTo(1, 2))
print(p.get_length())  # 2.23606797749979
p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
print(p.get_length())  # 28.191631669843197
m = p.get_path()
print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True

h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
print(h.get_length())  # 71.8992593599813

k = PathLines()
print(k.get_length())  # 0
print(k.get_path())  # []