# here are some practice questions to improve my logic 
 
#  Write a program to determine the maximum of two numbers using the ternary operator.

num1=10
num2=20

num3="num1 is greater"if num1>=num2 else "num2 is greater than num1 "
print(num3)


#  Create a program that checks whether a given number is positive, and  negative,  using the ternary operator.


num=int(input("Enter a number :\n"))

num1="number is positive"if num>=0 or "number is negative " else "number is negative " 

print(num1)


#  Write a Python program to check if a person is eligible to vote based on their age (18 or above) using the ternary operator.

age=int(input("Enter your age"))
result="you are eligible to vote " if age>=18 else "you are not eligible to vote "
print(result)


# if else statement practice questions 

#  Create a program that determines the largest among three numbers.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print("num1 is greatest")
elif num2 >= num1 and num2 >= num3:
    print("num2 is greatest") 
else:
     print("num3 is greatest")


# Write a Python program that checks whether a given year is a leap year or not using if-else statements.

num1 = int(input("Enter the number: "))

if num1%4==0:
    print("it is a leap year")
else:
    print("it is not a leap year")    



