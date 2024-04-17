# Here in this file we learn about recursion

# Recursion is simply defined as when a function calls itself repeatedly

def show(n):
    if n==0: # This is called base casae
        return
    print(n)
    show(n-1)  
show(5)    


# factorial example

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)

print(factorial(5))    
print(factorial(4))    
print(factorial(3))    
    
