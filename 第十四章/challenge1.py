class Square:
    square_list = []

    def __init__(self, name):
        self.name = name
        self.square_list.append(self.name)

squ = Square("kel")
print(squ.square_list)
