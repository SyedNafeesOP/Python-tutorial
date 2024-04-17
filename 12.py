# In this file we improve our logic in python b using loops

# *
# **
# ***
# ****
# *****


for i in range(1, 6):
    print('*' * i)


####
####
####
####



for i in range(4):  
    print('#'* 4) 

# Write a Python program to print the numbers from 1 to 10 using a for loop.

# by for loop

for i in range (1,10):
    print(i)


print("loops ")
# by while loop 

i=1
while i<=10:
    print(i)
    i+=1

#  Write a Python program to calculate the sum of all the numbers from 1 to 10 using a for loop.


sum=0
for i in range(1,11):
    sum+=i
    print(sum)

    # Write a Python program to print the even numbers from 1 to 20 using a while loop


i=0
while i <=20:
    i+=1
    if i %2==0:
        print(i)
        

# Write a Python program to find the factorial of a given number using a for loop
f = 1
val = int(input("Enter a number: "))
for i in range(1, val + 1):
    f *= i
print("Factorial of", val, "is", f)





