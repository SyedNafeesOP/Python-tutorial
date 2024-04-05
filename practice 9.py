# practice questions with while loop 

# print number from 1 to 100

i=1
while i<=100:
    print(i)
    i=i+1

# print number from 100 to 1
print("Another example")

i=100
while i >=1:
    print(i)
    i-=1

# print the elements of the following list using a loop
#[1,4,9,16,25,36,49,64,81,100]

list=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx < len(list):
    print(list[idx])
    idx +=1



#  print the elements of the following tuple using a loop
tup=(1,2,3,4,5,6,7,8)
idx=0
while idx < len(tup):
    print(tup[idx])
    idx+=1


# print the multiplication table of number n 
num = int(input("Enter a number: "))
temp=0
i=0
while i < 10:

    temp=temp+num
    i+=1
    print(temp)

# another logic

i=1
while i<=10:
    
    print(10*i)
    i+=1


# another logic
n = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

# wap to search for a number
#  x in this tuple using loop
num=(1,4,9,16,25,36,49,64,81,100)
x=25
i=0
while i < len(num):
    if (num[i] == x):
        print("found at idx",i)
    i+=1

# Write a program that prints all the even numbers from 1 to 20 using a while loop.

i=0
while i<=20:
    if i%2==0:
        print(i)
    i+=1    