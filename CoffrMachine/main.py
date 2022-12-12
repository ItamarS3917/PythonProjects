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


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money ${profit}")


def make_coffee(user_choice):
    """get the user chouce and make coffee for the user
    returns the cost to caller and adds the cost to profit"""
    for item in MENU[user_choice]['ingredients']:
        resources[item] -= MENU[user_choice]['ingredients'][item]
    return MENU[user_choice]['cost']


def check_resource(coffee_type):
    """Check Machine resources before each use and return True if we can operate
        the machine otherwise return False"""
    for item in MENU[coffee_type]['ingredients']:
        if MENU[coffee_type]['ingredients'][item] > resources[item]:
            return False
    return True


def return_missing_resource(coffee_type):
    for item in MENU[coffee_type]['ingredients']:
        if MENU[coffee_type]['ingredients'][item] > resources[item]:
            return item
    return item  # by default return the last item in resources list


def process_coins(amount_due):
    """Get the money from the user and checks if the use enter the correct amount of money.
        if the user insert the exact amount due the method returns 0
        if the user inserted more then he needs the method return the change
        otherwise return -1"""
    change = 0

    print("Please insert coins.")
    q_inserted = float(input("how many quarters?")) * 0.25
    d_inserted = float(input("how many dimes?")) * 0.10
    n_inserted = float(input("how many nickles?")) * 0.05
    p_inserted = float(input("how many pennies?")) * 0.01

    sum_coins_inserted = q_inserted + d_inserted + n_inserted + p_inserted

    if sum_coins_inserted == amount_due:
        return change
    elif sum_coins_inserted > amount_due:
        change = round(sum_coins_inserted - amount_due, 2)
        return change
    else:  # sum_coins_inserted < amount_due
        return -1


def prompt_user(user_choice):
    coins = 0
    if user_choice == 'report':
        print_report()
        return 0

    elif check_resource(user_choice):
        coins = process_coins(MENU[user_choice]['cost'])

        if coins == 0:
            print(f"Here is your {user_choice}. Enjoy!")
            return make_coffee(user_choice)
        elif coins > 0:
            print(f"Here is ${coins} in change.")
            print(f"Here is your {user_choice}. Enjoy!")
            return make_coffee(user_choice)
        else:  # The user didn't pay the espresso price
            print("Sorry. that's not enough money. Money refunded.")
            return 0  # return 0 to add 0 to money counter
    else:  # The machine doesn't have enough resources to make that drink
        missing_resource = return_missing_resource(user_choice)
        print(f"Sorry there is not enough {missing_resource}.")
        return 0


game_over = False
profit = 0
while not game_over:
    prompt = input("What would you like?(espresso\latte\cappuccino):")
    if prompt != 'off':
        profit += prompt_user(prompt)
    else:  # The user want to end the machine operation
        game_over = True
