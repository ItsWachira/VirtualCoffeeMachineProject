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
# ItemInMenu= []
# for item in MENU:
#   MenuItem = MENU[item]
#   for menu_item in MenuItem:
#     M_Item = MenuItem[menu_item]
#     for mItem in M_Item:
#       m_item = M_Item[mItem]
#       print(m_item)

# capture the customer's coffee type order


RemainingResources = []

# latte
Lattewater = MENU["latte"]["ingredients"]["water"]
latteMilk = MENU["latte"]["ingredients"]["milk"]
latteCoffee = MENU["latte"]["ingredients"]["coffee"]
CostLatte = MENU["latte"]["cost"]

# expresso
espressowater = MENU["espresso"]["ingredients"]["water"]
espressoCoffee = MENU["espresso"]["ingredients"]["coffee"]
espressoCost = MENU["espresso"]["cost"]

# cappuccino
cappuccinowater = MENU["cappuccino"]["ingredients"]["water"]
cappuccinoMilk = MENU["cappuccino"]["ingredients"]["milk"]
cappuccinoCoffee = MENU["cappuccino"]["ingredients"]["coffee"]
Costcappucino = MENU["cappuccino"]["cost"]

# resources
resourceWater = resources["water"]
resourceMilk = resources["milk"]
resourceCoffee = resources["coffee"]

customer_input = input("What would you like? (espresso/latte/cappuccino)")
# obtain the amount they deposit in the machine
print("Please insert coins.")
# quarters 25 cent $0.25
quarters = int(input("how many quarters?: "))
New_quarter = quarters * 0.25
# dimes 10 cents  $0.10
dimes = int(input("how many dimes?: "))
New_dimes = dimes * 0.10
# nickles 5 cents  $0.05
nickles = int(input("how many nickles?: "))
New_nickels = nickles * 0.05
# pennies 1 cent $0.01
pennies = int(input("how many pennies?: "))
New_pennies = pennies * 0.01

# total customer coins
total_Amount = New_quarter + New_dimes + New_nickels + New_pennies
print(total_Amount)


def latte():
    NewWaterAmount = resourceWater - Lattewater
    RemainingResources.append(NewWaterAmount)

    NewMilk = resourceMilk - latteMilk
    RemainingResources.append(NewMilk)

    NewCoffee = resourceCoffee - latteCoffee
    RemainingResources.append(NewCoffee)

    AmountBalance = round(total_Amount - CostLatte, 2)

    print("Have yourself a wonderful drink!!")
    print(f"You cash balance is {AmountBalance}")
    print(RemainingResources)


def espresso():
    NewWaterAmount = resourceWater - espressowater
    RemainingResources.append(NewWaterAmount)

    NewCoffee = resourceCoffee - espressoCoffee
    RemainingResources.append(NewCoffee)

    AmountBalance = round(total_Amount - espressoCost, 2)

    print("Have yourself a wonderful drink!!")
    print(f"You cash balance is {AmountBalance}")
    print(RemainingResources)


def cappuccino():
    NewWaterAmount = resourceWater - cappuccinowater
    RemainingResources.append(NewWaterAmount)

    NewMilk = resourceMilk - cappuccinoMilk
    RemainingResources.append(NewMilk)

    NewCoffee = resourceCoffee - cappuccinoCoffee
    RemainingResources.append(NewCoffee)

    AmountBalance = round(total_Amount - Costcappucino, 2)

    print("Have yourself a wonderful drink!!")
    print(f"You cash balance is {AmountBalance}")
    print(RemainingResources)


if customer_input == "latte":
    if total_Amount > CostLatte:
        latte()
    else:
        print("Not enough money to buy coffee!!")
elif customer_input == "espress":
    if total_Amount > espressoCost:
        espresso()
    else:
        print("Not enough money to buy coffee!!")
else:
    if total_Amount > Costcappucino:
        cappuccino()
    else:
        print("Not enough money to buy coffee!!")
