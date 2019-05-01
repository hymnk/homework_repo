class Horse:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

ride = Rider("kel")
hors = Horse("VIlland", ride)
print(hors.owner.name)
print(hors.name)