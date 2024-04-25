# Important concept for oops

# Abstraction

# Abstraction in OOP refers to the process of hiding the complex implementation details and showing only the essential features of the object. It allows programmers to focus on what an object does rather than how it does it.
class Car:
    def __init__(self) :
        self.acc=False
        self.brake=False
        self.clutch=False
        
    def start(self):
        self.clutch=True
        self.acc=True

        print("Car started")

car1=Car()
car1.start()


# Encapsulation
#Encapsulation is another key concept in object-oriented programming (OOP) that complements abstraction. It refers to the bundling of data (attributes or properties) and methods (functions or procedures) that operate on the data into a single unit or class. The primary goal of encapsulation is to hide the internal state of an object from the outside world and only allow access to it through well-defined interfaces (methods).


# lets practice 

# Create account class with 2 attibutes - balance & account no  Create methods for debit credit and printing the balance


class account:
    def __init__(self,balance,accountno):
        self.balance=balance
        self.accountno=accountno
    def debit(self, amount):
        self.balance -= amount
        print("RS", amount, "was debited")
        print("Total balance =", self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("RS ",amount,"was credit")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance            

a1=account(10000,"567")
print(a1.balance)

a1.debit(1000)
a1.credit(500)
