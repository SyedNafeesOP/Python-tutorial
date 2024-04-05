
# expression  execution

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

name="ahmad"
age="27"
terms=10
print((name+age)*terms)


car = "nissan gtr"
price = 2800000000
status = 10

# Convert price and status to strings before multiplication
result = car * (price * status)

print(result)



#Write a Python program to swap two variables without using a temporary variable.

a = 10
b = 15
temp = a   # Store the value of a in temp
a = b      # Assign the value of b to a
b = temp   # Assign the value stored in temp to b

print(f"a after swapping:", a)  # Output the new value of a
print("b after swapping:", b)  # Output the new value of b



# To swap the values of two variables
# without using a temporary variable, you can use arithmetic operations.

a = 5
b = 10

# Swapping logic
a = a + b  # Step 1
b = a - b  # Step 2 (new value of a - original value of b)
a = a - b  # Step 3 (new value of a - new value of b)

print("a after swapping:", a)
print("b after swapping:", b)
