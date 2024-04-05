# conditional statement 
# let us understand conditional statement with traffic light examples

light=input("light :\t")
if light=="green":
    print("go")
elif light=="yellow":
    print("look and ready ")
elif light=="red":
    print("stop")    
else:
    print("light is broken ")    


#  another example to understand if else by grading students


marks=int(input("marks : \t"))

if marks >= 90 :
    print("you get A grade")

elif marks >= 80 :
    print("you get B grade")
elif marks >= 70 :
    print("you get C grade")
elif marks >= 60 :
    print("you get D grade")
else:
    print(" you are fail ")    
              



