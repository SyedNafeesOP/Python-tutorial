# lists in python 

marks=[94.4,90,60,70,45]
print(marks)
# indexing

print(marks[0])
print(marks[1])
print(len(marks))

# lists are mutable

student=["Nafees",94,15,"Jaranwala"]
print(student)
student[1]=95.5
print(student)


# slicing 
   
marks=[56,78,96,67,89]
print(marks[:3])
print(marks[4])
print(marks[-4:-1])

# list Methods

list=[11,4,5,6,7]
print(list.append(9))# add element at the last
print(list)

print(list.sort()) # sort the value in ascending order
print(list)


print(list.sort(reverse=True)) #sort the value in descending order
print(list)


print(list.insert(0,"nafees")) # add and element  at index
print(list)


print(list.reverse())# reverse the list
print(list)

print(list.remove(5))# remove first occurence of element
print(list)


print(list.pop(2))# removes element as index 
print(list)