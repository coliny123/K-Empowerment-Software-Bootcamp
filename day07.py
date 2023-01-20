#10_4

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


e = Element("Hydrogen", "H", 1)

print(e.name, e.symbol, e.number)