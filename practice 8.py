
# Write a Python program to store and display the details of a student using a dictionary. The details should include the student's name, age, course, and grades in three subjects: Math, Science, and English.

# Ask the user to input the student's details.
# Store these details in a dictionary.
# Print out the dictionary containing the student's details.



# details

name=input("enter your name :\n")
age=int(input("enter your age :\n"))
course=input("enter your course :\n")
math_grade = int(input("Enter Math grade: "))
science_grade = int(input("Enter Science grade: "))
english_grade = int(input("Enter English grade: "))


student_details={
    "name":name,
    "age":age,
    "course":course,
    'Math': math_grade,
        'Science': science_grade,
        'English': english_grade
}
print(student_details)



# store the following word meanings in a python dictionary

dict={
    "cat":"a small animal",
    "Table":["a piece of furniture ","lists of facts and figures"]

}
print(dict)

# sets practice and tutorial


num={1,2,3,4,5}
print(type (num))
print(num)

# empty set

num=set()
print(num)

# methods

num.add(1)# add the value in empty set
num.add(2)# add the value in empty set
print(num)

num.remove(2)# remove the value

num={2,2,2}
print(num)# in set one element is count by one just like {2,2,2} answer is 2


# sets pracice 

# you are given a list of subjects for students . Assume one classroom is required for 1 subject. how many classroom are needed by all subjects

#"python","java","C++","python","javascript","java","python ","java","C++","C"

subjects={
    "python","java","C++","python","javascript","java","python ","java","C++","C"
}

print(len(subjects))
print(subjects)


# figure out a way to store 9 and 9.0 as separate values in the set (
# you can take help of using built in datatypes)


value={
    9,"9.0"
}
print(value)

# another way
value={
    "9",9.0
}
print(value)

# another way

value={("int",9),
("float",9.0)
}

print(value)
print(type(value))


