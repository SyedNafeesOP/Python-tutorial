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

print(s1.college_name)
# class and instance attributes

