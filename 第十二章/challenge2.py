import math

class Circle:
    def __init__(self, h):
        self.hankei = h
    
    def area(self):
        return (self.hankei * 2) * math.pi

cle = Circle(5)
print(cle.area())