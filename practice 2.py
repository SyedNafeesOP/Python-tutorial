# write a program that asks for user for their name and age then prints out a message them by name and telling how old they will be next year 

name=input("enter your name :\n")
age=int(input("enter your age :\n"))

nextyear=age+1

print("next year your age is ",nextyear)

# write a program that converts a temperature in celcius to fahrenheit

temp=int(input("Enter temperature in celcius:\n "))

fahrenheit=((temp*9/5)+32)

print("temperature in fahrenheit is ", fahrenheit)

#write a program that calculate area of a rectangle

length=int(input("Enter length of rectangle:\n "))

width=int(input("Enter width of rectangle:\n "))

area=length*width
print("the area of rectangle is ",area)


# Create a program that asks the user to enter their first name and last name separately, then prints out their full name.

first_name=input("enter your first name :\n")
last_name=input("enter yor last name:\n")
name=first_name+last_name
print("your full name is ",name)

# Write a Python program that calculates the average of three numbers entered by the user.

a=19
b=12
c=56
avg=(a+b+c)/3
print(avg)

# Develop a program that takes a user's weight in kilograms and height in meters, then calculates and prints their BMI (Body Mass Index). (Formula: BMI = weight / (height * height))
weight=int(input("enter weight in kilograms :\n "))

height=int(input("enter height in meters :\n "))

BMI=(weight/(height*height))
print(BMI)


# Create a program that asks the user to enter their age and then calculates the age in months, days, hours, and minutes.

age=int(input("Enter your age :\n"))

months=12*age
print("your age in months is ", months)
print(months)


days=365*age
print("your age in days is ", days)
print(days)

hours=24*days
print("your age in hours ",hours)
print(hours)

minutes=hours*60
print("your age in minutes ",minutes)
print(minutes)

# Write a program that takes a user's name and favorite number, then prints out a message saying "Hello [name]! Your favorite number is [number]."
name=input("enter your name ")
number=input("enter your favourite number:")
print("HELLO",name)

print("your favourite number is ",number)

