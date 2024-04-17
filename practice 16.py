# Create a new file "practice .txt" using python . Add the following data in it:

# Hi everyone
# we are learning File I/O
# using python
# I like programming in Python

with open("practice .txt","r+") as f:
    print(f.write("Hi everyone\nwe are learning File I/O\n using python \n I like programming in python"))
    data=f.read()
    print(data)


# Waf that replaces occurences of python with  java in above file

with open("practice .txt","r+") as f:
    data=f.read()
    newdata=data.replace("python","Java")
    f.write(newdata)
    print(newdata)



