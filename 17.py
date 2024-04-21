# Write a function that takes two numbers as input and returns their sum.

# def sum():
#     num=int(input("Enter a number : "))
#     num1=int(input("Enter a number : "))
#     return num+num1
# print(sum())
    
# Create a function that takes a list of numbers as input and returns the maximum and minimum numbers in the list.    

# def maximum(num1,num2,num3):
    
#     if num1>num2 and num1>num3:
#         print("num1 is greatest")
#     elif num2>num1 and num2>num3:
#         print("num2 is greatest")
#     else:
#         print("num3 is greatest")
        
    


# num1=int(input("Enter first number : "))  
# num2=int(input("Enter second number :"))  
# num3=int(input("Enter third number : "))  

# print("maximum",maximum(num1,num2,num3))
# def minimum(num1,num2,num3):
#     if num1<num2 and num1<num3:
#         print("num1 is smaller")
#     elif num2<num1 and num2<num3:
#         print("num2 is smaller")
#     else:
#         print("num3 is smaller")


           
# num1=int(input("Enter first number : "))  
# num2=int(input("Enter second number :"))  
# num3=int(input("Enter third number : "))  
       
# print("minimum",minimum(num1,num2,num3))       



# Create a function that takes a list of numbers as input and returns the maximum and minimum numbers in the list.

# Function to find the maximum number in the list
def maximum(numbers):
    return max(numbers)

# Function to find the minimum number in the list
def minimum(numbers):
    return min(numbers)

# Get the list of numbers from the user
numbers = []
num = int(input("Enter the number of elements in the list: "))
for i in range(num):
    num_input = int(input(f"Enter number {i+1}: "))
    numbers.append(num_input)

# Print the maximum and minimum numbers in the list
print("Maximum: ", maximum(numbers))
print("Minimum: ", minimum(numbers))