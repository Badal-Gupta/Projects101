MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

def is_resource_ok(order_ingredients):
    """true if order can be make false if ingredients are not sufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coin():
    """total calculated from coin inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dines?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_money_enough(money_received, drink_cost):
    """Return True if money is enought return false if the amount given is not sufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        global profit
        profit += drink_cost
        print(f"Here is ${change} is your change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

profit = 0
flag = True
while flag:
    user = input("What would you like? (espresso/latte/cappuccino): ")
    if user == "off":
        flag = False
    elif user == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user]
        if is_resource_ok(drink["ingredients"]):
            payment = process_coin()
            if is_money_enough(payment,drink["cost"]):
                make_coffee(user,drink["ingredients"])



