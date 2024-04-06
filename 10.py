# Break and continue statement 

i=1
while i <=5:
    print(i)
    if i==3:
        break
    i+=1
print("1st loop ended ")
m=2
while m<=30:
    
    if m%2==0:
        print(m)

    if m==24:
        break    
    m+=1

# continue statement 
    

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue # acts as skip
    print(i)
    i += 1



