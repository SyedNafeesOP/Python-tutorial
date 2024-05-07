# del keyword

class student:
    def __init__(self,name):
        self.name=name
s1=student("nafees")
# del s1.name
print(s1.name)

# private and public attribute
# __ by using double underscore we can make private attribute

class Account:
    def __init__(self,acc,pas):
        self.acc=acc
        self.__pas=pas # private

    def reset(self):
        print(self.__pas)    

acc1=Account("47836","NAFEES")
print(acc1.acc)
#print(acc1.__pas)

acc1.reset()


# inheritance

class Dreamcar():
    def __init__(self, fuel, horsepower, brand):
        self.fuel = fuel
        self.horsepower = horsepower
        self.brand = brand

    @staticmethod
    def car():
        print("NISSAN GTR")

    def info(self):
        print(f"Brand: {self.brand}, Fuel: {self.fuel}, Horsepower: {self.horsepower}")


class Porsche(Dreamcar):
    def __init__(self, name, fuel, horsepower):
        super().__init__(fuel, horsepower, "Porsche")
        self.name = name


car1 = Dreamcar("petrol", 600, "Bugatti")
car2 = Porsche("2023 Porsche 911", "petrol", 450)

car1.car()
car1.info()

car2.car()
car2.info()

# Again learning oops 

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def fullname(self):
        return f"{self.brand}{self.model}"

c1=Car("Mercedes","S class")
print(c1.brand)
print(c1.model)

c2=Car("BMW","M5")
print(c2.brand)
print(c2.model)

print(c1.fullname())
print(c2.fullname())


class ElecricCar(Car):
    def __init__(self, brand, model,batterysize):
        super().__init__(brand, model)
        self.batterysize=batterysize

    
e1=ElecricCar("Tesla","Model S","85kWH")    
print(e1.brand)
print(e1.model)
print(e1.batterysize)
print(e1.fullname())

