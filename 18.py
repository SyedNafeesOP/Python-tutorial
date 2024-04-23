# # oops in python
# # Basically oops is important for programming


# # Class and objects in python
# # create class

# class Student:
#     name="Nafees"
#     footballer="Ronaldo"
   
# # creating object    
# s1=Student()
# print(s1.name)
# s2=Student()
# print(s2.footballer)

# # Another class

# class Car:
#     name="Nisangtr"
#     price="28 'crores'"
#     horsepower=600 

# c1=Car()
# print(Car.name)

# Constructor 
# __init__()is constructor

class student:
    college_name="Punjab college"
    def __init__(self,name,marks ) :
        print("Adding some data about student and his marks")
        self.marks=marks
        self.name=name
              

s1=student("Ahmad",97)
print(s1.name)
print(s1.marks)


s2=student("Haider",95)
print(s2.name)
print(s2.marks)

print(s2.college_name)

# class and instance attributes
# Class Attributes:
# Class attributes are attributes that are shared by all instances of a class.
# They are defined inside the class definition but outside of any methods.
# Class attributes are accessed using the class name or an instance of the class.
# They are typically used to store data that is common to all instances of the class.
# Example:

# python

class Car:
    # Class attribute
    wheels = 4

    def __init__(self, make, model):
        self.make = make  # Instance attribute
        self.model = model  # Instance attribute

# Accessing class attribute
print(Car.wheels)  # Output: 4

# Creating instances
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Accessing instance attributes
print(car1.make, car1.model)  # Output: Toyota Camry
print(car2.make, car2.model)  # Output: Honda Civic

# Accessing class attribute through instance
print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4
# Instance Attributes:
# Instance attributes are specific to each instance of a class.
# They are defined inside the constructor method (__init__) using self.
# Instance attributes belong to individual objects (instances) and are not shared between instances.
# They can be accessed and modified using instance variables.
# Example:

# python

class Dog:
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

# Creating instances
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing instance attributes
print(dog1.name, dog1.age)  # Output: Buddy 3
print(dog2.name, dog2.age)  # Output: Max 5

# Understanding the difference between class attributes and instance attributes is crucial for effective object-oriented programming in Python.







