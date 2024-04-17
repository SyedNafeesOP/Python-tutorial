# # File input/output

# # reading a file
# f=open("sample.txt","r")

# # data=f.read()

# # if we applay f.read() than it print all not a single line
# # Else it print single line 

# line1=f.readline()
# print(line1)
# f.close()

# # print(data)
# # print(type(data))

# # writing a file 

# file=open("sample.txt","a")
# file1=file.write(" Basically python is an important thing for ML and AI") 
# print(file1)
# file.close()

# f1=open("demo.txt","w")
# print(f1.write("Python has many advantages\nIt is easy to learn \nresources are availible easily"))
# f.close()

# # combining  reading and writing

# f=open("demo.txt","r+")
# print(f.write("Python is a programming language"))
# print(f.read())
# f.close()

# # by using w+ file is trancuate means all the data has been removed


# f=open("demo.txt","a+")
# print(f.write("Python is a programming language"))
# print(f.read())
# f.close()

# with syntax

# with open("demo.txt","r")as f:
#     data=f.read()
#     print(data)

# with open("demo.txt","a+")as f:
#     print(f.write("\nAfter this i learn DSA for better understanding"))
#     data=f.read()
#     print(data)


# deleting a file 
# we need to create a sample file for deleating
with open("1.txt","w")as f:
    print(f.write("this is a sample file "))



# we need to download a module
import os
# print(os.remove("1.txt"))
