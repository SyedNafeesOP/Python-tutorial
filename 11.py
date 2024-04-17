 # for loops in python

# for loops are used to get sequece of values

num=[1,2,3,4]

for idx in num:
    print(idx)

print("End of outer loop")



num=["python","Java","C++"]

for idx in num:
    print(idx)


players=("CRISTIANO RONALDO","VINICIOUS  ","OZIL","BALE","MESSI")
for player in players:
    print(player)
    print(type(players))


str="python"
for char in str :
    print(char)


# we can use optional elsein loops

str="python"
for char in str :
    if char=="o":
        print("o found")
        break
    print(char)
else:
    print('END')

    
# range function

for i in range(10):
    print(i)


for i in range(2,10):
    print(i)


for i in range(2,10,2):
    print(i)
