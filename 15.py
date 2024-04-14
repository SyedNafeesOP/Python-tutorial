# # The Fibonacci Sequence

# def seq(f1,f2):
   
#     f3=f1+f2
#     print("The Fibonacci Sequence is",f3)
 

# seq(4,5)


# # square of Number 

# def square():
#     num=int(input("Enter a numer : \n"))
#     result=num*num
#     return result
# result=square() 
# print("square of number is ",result)


# WAP to table of a number

def Table():
    num=int(input("Enter a numer : \n"))
    i=0
    while i<=10:
        print(f"{num} x {i} = {num * i}")
        i+=1
        
        
result=Table()
print("Table of number is ",result)