# dictionary in python

dict={
    "name":"Nafees",
    "marks":1130,
    "class":10
}
print(dict)
print(type(dict))

# we can also  create list and tuples in dictionary 
info={
    "name":"Nafees",
    "language":"python",
    "age":15,
    "field":["Data Science","Machine Learning","AI","Web development"],  
    "courses":("Apna college ","Code with harry")
}

print(info)

# dictionary are mutable

# aceess value in dictionary

print(info["age"])
print(info["courses"])
print(info["field"])

# we can also change the value in dictionary because they are mutable

info["name"]="Ahmad"
print(info)

# another example
dict["class"]=11
print(dict)


goat={
    "Football":["Ronaldo","Pele","Ozil","Zidane"],
    "Cricket":("Virat Kholi","Gayle","AB","Wasim akram"),
    "Basketball":"Michal jordan,LebronJames",

}

print(goat)
print(type(goat))

#we can also create a empyty dictionary

empty_dict={

}
print(empty_dict)

# nested dictionary

student={
    "name":"Nafees",
    "score" : {
        "chem":56,
        "phy":58,
        "math":70,        
    }

}

print(student["score"])
print(student["score"]["chem"])


# dictionary methods

print(student.keys())# return keys
print(list(student.keys()))# return keys in list


print(student.values())# return values

print(student.items())# returns all (key ,val) pairs as tuples 

print(student.get("score"))# return key according to value 


print(student.update({
    "city":"jaranwala"
}))# inserts the specified itemes to a dictionary

print(student)

