class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, widths):
        if type(widths) == int and 0 <= widths <= 10000:
            self.__width = widths
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, heights):
        if type(heights) == int and 0 <= heights <= 10000:
            self.__height = heights
            self.show()


wnd = WindowDlg("Диалог 1", 100, 50)
wnd.width = 10
wnd.height =200
