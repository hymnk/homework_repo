class Shape:
    def __init__(self, w=10, h=30):
        self.width = w
        self.height = h

    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def calclate_perimeter(self):
        return self.width * self.height * 2

class Square(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    def calclate_perimeter(self):
        return self.width * 4

rect = Rectangle(20, 40)
rect.what_am_i()