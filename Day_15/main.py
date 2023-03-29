MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def reso_man(ask_coffee):
    
    temp=MENU[ask_coffee]
    temp_ingred=temp["ingredients"]
    for i in temp_ingred:
        if resources["water"]<temp_ingred["water"]:
            print("Sorry there is not enough water.")
            return 0
        elif resources["milk"]<temp_ingred["milk"]:
            print("Sorry there is not enough milk.")
            return 0
        elif resources["coffee"]<temp_ingred["coffee"]:
            print("Sorry there is not enough coffee.")
            return 0
        else:
            resources["water"]-=temp_ingred["water"]
            resources["milk"]-=temp_ingred["milk"]
            resources["coffee"]-=temp_ingred["coffee"]
            return 1
def coins_debit(ask_coffee):
    quarters=float(input("How many quarters? :-"))*25/100
    dimes=float(input("How many dimes? :-"))*10/100
    nickles=float(input("How many nickles? :-"))*5/100
    pennies=float(input("How many pennies? :-"))/100
    money=quarters+dimes+nickles+pennies
    temp=MENU[ask_coffee]
    global balance
    balance+=temp["cost"]
    if money<temp["cost"]:
        print("U dont have enough coin to buy this kind of coffee go home and drink water only")
        global end
        end=1
    money-=temp["cost"]
    return money
balance=0
end=0
while end==0:
    ask_coffee=input("What would you like? (espresso/latte/cappuccino):")
    if ask_coffee=="espresso":
        if reso_man(ask_coffee)==1:
            print("here is ur change: $",coins_debit(balance,ask_coffee))
            print(f'Here is your {ask_coffee} ☕️. Enjoy!')
            continue
        else:
            continue
    elif ask_coffee=="latte":
        if reso_man(ask_coffee)==1:
            print("here is ur change: $",coins_debit(balance,ask_coffee))
            print(f'Here is your {ask_coffee} ☕️. Enjoy!')
            continue
        else:
            continue
    elif ask_coffee=="cappuccino":
        if reso_man(ask_coffee)==1:
            print("here is ur change: $",coins_debit(balance,ask_coffee))
            print(f'Here is your {ask_coffee} ☕️. Enjoy!')
            continue
        else:
            continue
    elif ask_coffee=="report":
        for i in resources:
            print(resources[i])
        print(f"Money: ${balance}")
    elif ask_coffee=="off":
        end=1
    else:
        print("Wrong input")
        continue
    