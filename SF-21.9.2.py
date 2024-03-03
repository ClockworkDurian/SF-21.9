class Rectangle:
    def __init__(self, x, y, width, heigth):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth

    def __str__(self):
        return f'Rectangle : {self.x}, {self.y}, {self.width}, {self.heigth}.'

    def get_area(self):
        return self.width * self.heigth


rect_1 = Rectangle(0, 0, 20, 10)
print(rect_1)
print(rect_1.get_area())