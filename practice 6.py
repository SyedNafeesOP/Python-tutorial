#Write a program to concatenate two lists.
list1=[1,2,3]
list2=[4,5,6]
list3=list1+list2
print(list3)

# Write a Python program to sum all the items in a list.

list=[1,2,3]

print(sum(list))

# Write a program to remove duplicates from a list.
list=[1,2,3,3,4,5]
print(list.remove(3))
print(list)

# Write a program to sort a list of integers in ascending order.

list=[2,3,5,1,4,8,9]
print(list.sort())
print(list)

# Write a program to reverse a list.

list=[2,3,5,1,4,8,9]
print(list.reverse())
print(list)

# Write a program to shuffle a list randomly.
import random

list=[1,2,5,6,7]
print(random.shuffle(list))
print(list)

# wap to ask the user to enter names of therir 3 favourite movies and store them in a list
list=[]
user1=input("Enter your first favourite movie ")
user2=input("Enter your second favourite movie ")
user3=input("Enter your third favourite movie ")
list=[user1,user2,user3]
print(list)

# we can also store in list by using append method


# wap to check if a list contains a palindrome of element 

list=[1,2,3,2,1]
list=(list.copy())
print(list)

reverse=list[::-1]
print(reverse)

if list==reverse:
     print("The list contains a palindrome.")
else:
    print("The list does not contain a palindrome.")



    