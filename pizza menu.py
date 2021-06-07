import sys

toppings = ["pepperoni", "pineapple", "Cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = ["$2", "$6", "$1", "$3", "$2", "$7", "$2"]

pizza_and_prices = [ [prices[0], toppings[0]], [prices[1], toppings[1]], [prices[2], toppings[2]], [prices[3], toppings[3]], [prices[4], toppings[4]], [prices[5], toppings[5]], [prices[6], toppings[6]] ]

num_two_dollar_slives = prices.count(2)
num_pizzas = len(toppings)
cheapest_pizzas = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[5]

def intro():
    print("welcome to (name) pizza place")
    print("We sell", num_pizzas, "different kinds of pizza!")

def menu():
    print("[1] show the menu")
    print("[2] leave")
    choose = int(input("Please select a option: "))
    if choose == 1:
        print(pizza_and_prices)
        print("[1] To see Cheapest pizza")
        print("[2] to see most expensive pizza")
        print("[3] Back to main menu")
        option = int(input("Please select a option: "))
        if option == 1:
            print(cheapest_pizzas)
            return
        elif option == 2:
            print(priciest_pizza)
        elif option == 3:
            menu()
        else:
            print("please selecet a vaild option")
            return
    elif choose == 2:
        print("Thanks for visting (name) pizza place")
        sys.exit()
    else:
        print("Please select the right option next time")
        menu()

menu()