# del keyword

class student:
    def __init__(self,name):
        self.name=name
s1=student("nafees")
# del s1.name
print(s1.name)

# private and public attribute
# __ by using double score we can make private attribute

class Account:
    def __init__(self,acc,pas):
        self.acc=acc
        self.__pas=pas # private

    def reset(self):
        print(self.__pas)    

acc1=Account("47836","NAFEES")
print(acc1.acc)
#print(acc1.__pas)

acc1.reset()
