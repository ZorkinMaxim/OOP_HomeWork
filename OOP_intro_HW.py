class Food:
    # pass
    def __init__(self, name, price, quantity, weight):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.weight = weight
    def __str__(self):
        return f"{self.name:>10} - {self.price:<5} MDL, {self.quantity:<2} pcs, {self.weight:<5} g"

class Drink:
    # pass
    def __init__(self, name, price, quantity, volume):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.volume = volume
    def __str__(self):
        return f"{self.name:>10} - {self.price:<5} MDL, {self.quantity:<2} pcs, {self.volume:<5} ml"

# def newFood(name, price, quantity, weight):
#     food = Food()
#     food.name = name
#     food.price = price
#     food.quantity = quantity
#     food.weight = weight
#     return food

# def newDrink(name, price, quantity, volume):
#     drink = Drink()
#     drink.name = name
#     drink.price = price
#     drink.quantity = quantity
#     drink.volume = volume
#     return drink

def printFood(food):
    print(f"{food.name:>10} - {food.price:<5} MDL, {food.quantity:<2} pcs, {food.weight:<5} g")

def printDrink(drink):
    print(f"{drink.name:>10} - {drink.price:<5} MDL, {drink.quantity:<2} pcs, {drink.volume:<5} ml")

def printItem(item):
    if type(item) is Food:
        printFood(item)
    elif type(item) is Drink:
        printDrink(item)



# f1 = newFood('Pizza', 100.00, 3, 250.00)
# d1 = newDrink('Juice', 35.00, 3, 100.00)
f1 = Food('Pizza', 100.00, 3, 250.00)
d1 = Drink('Juice', 35.00, 3, 100.00)

printItem(f1)
printItem(d1)
print(f1)
print(d1)




