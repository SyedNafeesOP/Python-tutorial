# we are making a restaurent menu type project 

menu={
    "Pizza":1300,
    "pasta":500,
    "Burger":350,
    "Cofee":200,
    "Fries":700,

}

print(menu)

customer=input("Tell me what you want to order : ")

if customer in menu:
    print("Your order has been added:")
    print(f"Your price is {menu[customer]}")
    print("Thanks for the order")
else:
    print("We have many other things")
    print("Do you want to order other things")
