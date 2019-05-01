class Square:
    def __init__(self, w):
        self.width = w
    
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.width, self.width, self.width, self.width)

squ = Square("5")
print(squ)
