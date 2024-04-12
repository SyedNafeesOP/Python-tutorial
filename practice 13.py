# function to calculate average of three numbers

def average(a,b,c):
    return (a+b+c)/3

average=average(98,97,95)
print(average)

# Write a function called reverse_string that takes a string as input and returns the reverse of that string. For example, if the input is "hello", the function should return "olleh".

def reverse_string(str): 
    return(str[::-1])

reverse_string=reverse_string("hello")
print(reverse_string)


# write a function to print the length of list 

num=[1,2,3,4,5,6]
cites=["Jaranwala","Faislabad","Lahore"]
def list_items(num,cites):
    print(len(num))
    print(len(cites))
    

list_items(num,cites)

# write a program to print the list in single line

Prophets=["Mohammad","Adam","Musa","Ibrahim","Yousaf"]
def list_prophets(Prophets):
    for prophet in Prophets:
        print(prophet,end="")

list_prophets(Prophets)
    
print("\n")    
#   waf to print the factorial of n
n = 5  


def calculate(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)    
calculate(7)    

# write a function to print usd to pak

def converter(usd_val):
    pak_val=usd_val*277
    print(usd_val,"USD=",pak_val,"PAK")

converter(3)

 