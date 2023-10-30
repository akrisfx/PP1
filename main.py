import json

class item:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    def getName(self) -> str:
        return self.name
    def getPrice(self) -> int:
        return self.price
    
class dish(item):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price)
        self.weight = weight

class drink(item):
    def __init__(self, name, price, volume) -> None:
        super().__init__(name, price)
        self.volume = volume


def DishJsonToArr(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as in_file:
            a = 1
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


    