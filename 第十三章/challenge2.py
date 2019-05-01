class Square:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def size(self):
        return self.width * self.height

    def change_size(self, w, h):
        self.width = w
        self.height = h

squ = Square(20, 25)
print(squ.size())
squ.change_size(100, 139)
print(squ.size())