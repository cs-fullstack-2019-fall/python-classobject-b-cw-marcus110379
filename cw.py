def main():
    problem1()
    problem2()
    problem3()

# Create a class Dog. Make sure it has the attributes name, breed, color, gender. Create a function that will print all attributes of the class. Create an object of Dog in your problem1 function and print all of it's attributes.
class Dog:
    def __init__(self, name, breed, color, gender):
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender
    def printAll(self):
        print(f"{self.name}, {self.breed},{self.color},{self.gender}") # !! : use string formatting to take advantage of f strings 
def problem1():
    myDog = Dog("Rocky", "poodle", "black","male")
    myDog.printAll()

# Problem 2:
# We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with the equal sign. If the user doesn't enter the equal sign, ask them to input another string.
def user():
    userInput = input("enter a string")
    while userInput != "=":
        userInput = input("enter another string")
def problem2():
    user()

# Problem 3:
# Create a class Product that represents a product sold online. A product has a name, price, and quantity.
# The class should have several functions:
# a) One function that can change the name of the product.
# b) Another function that can change the name and price of the product.
# c) A last function that can change the name, price, and quantity of the product.
# Create an object of Product and print all of it's attributes.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def funcA(self, name): # !! : this is a bad function name
        self.name = name
    def funcB(self, name, quantity): # !! : this is a bad function name AND change the name and price of the product
        self.name = name 
        self.quantity= quantity
    def funcC(self, name, price, quantity): # !! : this is a bad function name
        self.name = name
        self.price = price
        self.quantity = quantity
def problem3():
    product1 = Product("genie", "$25", "1")
    print(product1.name, product1.price, product1.quantity)
    product1.funcA("test1a")
    print(product1.name, product1.price, product1.quantity)
    product1.funcB("test2a", "test2b")
    print(product1.name, product1.price, product1.quantity)
    product1.funcC("test3a", "test3b", "test3c")
    print(product1.name, product1.price, product1.quantity)

main()