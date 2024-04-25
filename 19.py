class Person:
    print("This class is about a person personal information")
    def __init__(self,name,age,country):
        self.name=name
        self.age=age
        self.country=country
        

c1=Person("Nafees",15,"Pakistan")  
def country():
    print("Soon it will be Germany")

print(c1.name)
print(c1.age)

print(c1.country)
country() 

c2=Person("Ahmad",28,"Germany")
print(c2.name)
print(c2.age)

print(c2.country)

# Methods of oops concept

# Methods are functions that belongs to objects

class Songs:
    def __init__(self,songs):
        self.songs=songs

    def attributes(self):
        print("This is a amazing song",self.songs)
    def artist(name):
       print("Arjit singh")


s1=Songs("Menu vida kro")
s1.attributes()
s1.artist()

# one practice concept

# Create student class that takes name & marks of 3 subjects as arguments in constructor  then create a method to print the average


class Student:
    print("Here are name of student and marks of student of 3 subjects ")
    def __init__(self,name,physics,chemistry,math):
        self.name=name
        self.physics=physics
        self.chemistry=chemistry
        self.math=math
    def average(self):
         
        avg=(self.physics+self.chemistry+self.math)/3
        print("Here is the average",avg)

s1=Student("Nafees",58,56,70)
print(s1.name)
print(s1.physics)
print(s1.chemistry)
print(s1.math)

s1.average()

# another method
class Student:
    print("Here are name of student and marks of student of 3 subjects ")
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        total = sum(self.marks)
        print("Hi", self.name, "your average score is", total / len(self.marks))

s2 = Student("Haider", [70, 78, 79])
s2.avg()  # Corrected call to the avg method

# static methods 
        
# Methods that dont use the self parameter (work at class level)

class car:
    def __init__ (self,name) :
        self.name=name

    # @staticmethod
    def amazing():
        print("amazing")

    amazing()   

c1=car("Mercedes")       
print(c1.name)
