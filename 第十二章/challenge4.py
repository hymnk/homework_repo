class Hexagon:
    def __init__(self, a):
        self.aline = a

    def calculate_perimeter(self):
        return self.aline * self.aline * 2.6

hexa = Hexagon(5)
print(hexa.calculate_perimeter()) 