



class Car:

    def __init__(self, make, model):
        self.__make = make
        self.__model = model
    def set__make(self, make):
        self.__make = make
    def get__make(self):
        return self.__make
    def set__model(self, model):
        self.__model = model
    def get__model(self):
        return self.__model
    def __str__(self):
        return f"{self.__make} {self.__model}"
    

car1 = Car("Volvo", "XC90")
car2 = Car("Volvo", "V60")
car3 = Car("Volvo", "S90")


print("Original Cars:")
print(car1)
print(car2)
print(car3)

car2.set__model("XC60")

print("\nAfter modifying the second car")
print(car1)
print(car2)
print(car3)





