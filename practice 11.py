
# print the elements of the following list using a Loop 

list=[1,4,9,16,25,36,49,62,81,100]
for i in list:
    print(i)


# search for a number x in this tuple using a loop    

tup = (1, 4, 9, 16, 25, 36, 49, 62, 81, 100)
x = 36
for index, value in enumerate(tup):
    if value == x:
        print("Found", x, "at index", index)
        break
    else:
        print(value)

# another logic

tup = (1, 4, 9, 16, 25, 36, 49, 62, 81, 100)
x = 36
idx=0
for i in tup:
    if i==x:
        print("number found at index",idx)
        break
    idx+=1


# range funtion
    
# print even numbers from 2 to 100    
for i in range(2,100,2):
    print(i)

# print odd numbers from 1 to 100  
for i in range(1,100,2):
    print(i)


# write a program to find the sum of 10 natural number
n=10
sum=0
for i  in range(1,n+1):

    sum+=i
print("total sum is equal to ",sum)    
