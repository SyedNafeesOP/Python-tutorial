# single line conditional statement
# also known as ternary operator

food=input("enter food :\n")
eat="yes" if food =="cake" else "no"
print(eat)

# another example

food=input("food:\n")
print("delecious") if food=="cake"or food == "jalebi" else print("i do not want to eat")

#another example

color = input("Enter traffic light color: ")

print("Go") if color == "green" else (print("Stop") if color == "red" else print("Proceed with caution"))



# clever if / ternary opeeator

# syntax

# <var>=(false , true)[<condition>]

  
# example

age=int(input("enter your age :\n"))
vote=("yes","no")[age<=18]
print(vote)

# another example

sal=float(input("enter your salary:\n"))

tax=sal*(0.1,0.2)[sal<=50000]
print(tax)

# operators 

# arithmetic opeartors

num=int(input("enter a number :\n"))
num2=int(input("enter a number :\t"))
print(num+num2) # + is arithmetic operator
print(num-num2) # - is arithmetic operator
print(num*num2) # * is arithmetic operator
print(num**num2) # ** is arithmetic operator # also known as power opeartor
print(num/num2) # / is arithmetic operator
print(num%num2) # % is arithmetic operator


# relational operator

# it gives result in True and False
a=50
b=20

print(a==b)
print(a>=b)
print(a!=b)
print(a<=b)

# assignment operator
# = is assignment operator

num=10
#num=num+1 # both statement have same result
#num+=1 # both statement have same result
#num*=5
#num**=5
#num%=5
#num/=5

# all are assingnment operator
print(num)


# logical opearator
# not is logical operator
a=10
b=5
print(not False)
print(not (a>b))
# and is logical operator
a=True
b=False
print(a and b )


# or operator
a=True
b=False
print(a or b )

