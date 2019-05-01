class Rectangle:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def calclate_perimeter(self):
        return self.a + self.b + self.c + self.d + self.e + self.f

class Square:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def calclate_perimeter(self):
        return self.a + self.b + self.c + self.d

rec = Rectangle(2,4,6,7,8,9)
print(rec.calclate_perimeter())
squ = Square(6, 3, 10, 30)
print(squ.calclate_perimeter())