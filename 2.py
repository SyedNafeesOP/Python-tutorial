# expression execuation

# string and numeric values can operate together with *

A,B=2,3
txt="@"
print(A*txt*B)
# ALSO WRITTEN AS

A,B=2,3
txt="@"
print(2*txt*3)
# we can also use the value


g=5
b=15
val="$"
print(g*val*b)

# string and string operate with +

a,b="2",3
txt="@"
print((a+txt)*b)


name="nafees"
age="15"
terms=6
print((age+name)*terms)

# // stands for integar division
# it gives result with float and int displayed as float
a=10
b=5.9
c=a//b
print(c)

A,B=3,4
C=5
print(A+B*C)



A,B=3,4
C=5
print(A/B)

# answer is float when we divide two integars

#// stands for integar devision

a,b=1.5,3
c=a//b
print(c+a/b)

# integar devision with float and int will give int displayed as float

# floor gives closest integar, which is lesser than or equal to the float value
 
a=10
b=5
c=a//b
print(c)


a=18
b=3.9
c=a//b
print(c)

# remainder is negative when denominator is negative 
a,b=5,7
c=a%b
print(c)

a,b=5,-2
c=a%b
print(c)

# comments are the statement in the program that are not executed

#single comment start with #

'''
multiline comment start with triple quotes 
'''

# there is a shortcut for comment multiline is ctrl + forwardlash

# input in python 

# string input
name=input("name :")


# float input
value=float(input("value :"))

#int input

value=int(input("value :"))

