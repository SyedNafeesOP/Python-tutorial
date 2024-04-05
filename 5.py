# Strings
# There are three methods to create a list
name="nafees"
age='15'
study='''computer science'''

print(name+age)


str1=" This is a string\n and we are writing string in python "
print(str1)
# \n is escape squences used to modify the format of output

# concatenation

str2="we are learning python "
print(str1+str2)

# length function len(str)
len1=(len(str1))
print(len1)

# empty space

final_str=str1+""+str2
print(final_str)

# indexing
name="Nafees"
age="15"

# syntax str[0]

print(name[2])
print(name)

# slicing 

# syntax

# str[starting index : ending index]

language="python"

print(language[0:4])

print(language[0:len(language)])

print(language[:5])

# negative slicing  

str="machine"
print(str[-5:-1])

# strings functions or methods

str="java"
print(str.endswith("va"))# return true is string ends with substr  "va" is substring"
print(str.endswith("eg"))# return false is string ends with substr  "eg" is substring"
# capitalize 1st character 

print(str.capitalize())

# replaces all occurences of old value to new value

print(str.replace("java","python"))

# returns 1st index of 1st occurrer

print(str.find("v"))

# counts the occurences of str
print(str.count("a"))
               
# lets practice

# wap to input user first name and print its length 

user_name=input("enter your first name :\t")

print(len(user_name))

#ap to find the occurence of $ in a string

dollor_sign=" hi ia am the $ os USA and $ in Australia  "

print(dollor_sign.count("$")) 





