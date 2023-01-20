#10_8
class Element:
    def __init__(self, name, symbol, number):
        self.hidden_name = name
        self.hidden_symbol = symbol
        self.hidden_number = number

    def get_name(self):
        return self.hidden_name
    def get_symbol(self):
        return self.hidden_symbol
    def get_number(self):
        return  self.hidden_number


el_dict = {"name": "Hydrogen", "symbol": "H", "number": 1}

hydrogen = Element(**el_dict)

print(hydrogen.get_name(), hydrogen.hidden_symbol, hydrogen.hidden_number)