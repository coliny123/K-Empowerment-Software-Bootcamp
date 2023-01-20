#10_4
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def info(self):
        print(self.name, self.symbol, self.number)


el_dict = {"name": "Hydrogen", "symbol": "H", "number": 1}

e = Element(**el_dict)

print(e.info())