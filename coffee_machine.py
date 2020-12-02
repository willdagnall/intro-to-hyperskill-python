
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550


def base_coffee(water, milk, coffee_beans, disposable_cups, money):
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(coffee_beans) + " of coffee beans")
    print(str(disposable_cups) + " of disposable cups")
    print("$" + str(money) + " of money")
    print()
    actions(water, milk, coffee_beans, disposable_cups, money)

def actions(water, milk, coffee_beans, disposable_cups, money):
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == "exit":
            exit()
        if action == "buy":
            buy(water, milk, coffee_beans, disposable_cups, money)
        elif action == "fill":
            fill(water, milk, coffee_beans, disposable_cups, money)
        elif action == "take":
            take(water, milk, coffee_beans, disposable_cups, money)
        elif action == "remaining":
            print()
            base_coffee(water, milk, coffee_beans, disposable_cups, money)

def buy(water, milk, coffee_beans, disposable_cups, money):
    print()
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    buy_action = input()
    if buy_action == "1":
        if (water > 250 and coffee_beans > 16 and disposable_cups > 0):
            print("I have enough resources making you a coffee!")
            print()
            water -= 250
            coffee_beans -= 16
            money += 4
            disposable_cups -= 1
        elif(water < 250):
            print("Sorry, not enough water!")
            print()
        elif(coffee_beans < 16):
            print("Sorry, not enough coffee beans!")
            print()
        elif(disposable_cups < 1):
            print("Sorry, not enough disposable cups!")
            print()

    elif buy_action == "2":
        if (water >= 350 and milk >= 75 and coffee_beans >= 20 and disposable_cups >= 1):
            print("I have enough resources making you a coffee")
            water -= 350
            milk -= 75
            coffee_beans -= 20
            money += 7
            disposable_cups -= 1
            print()
        elif(water < 350):
            print("Sorry, not enough water!")
            print()
        elif(milk < 75):
            print("Sorry, not enough milk!")
            print()
        elif(coffee_beans < 20):
            print("Sorry, not enough coffee beans!")
            print()
        elif(disposable_cups < 1):
            print("Sorry, not enough disposable cups!")
            print()

    elif buy_action == "3":
        if (water >= 200 and milk >= 100 and coffee_beans >= 12 and disposable_cups >= 1):
            print("I have enough resources making you a coffee")
            water -= 200
            milk -= 100
            coffee_beans -= 12
            money += 6
            disposable_cups -= 1
            print()
        elif(water < 200):
            print("Sorry, not enough water!")
            print()
        elif(milk < 100):
            print("Sorry, not enough milk!")
            print()
        elif(coffee_beans < 12):
            print("Sorry, not enough coffee beans!")
            print()
        elif(disposable_cups < 1):
            print("Sorry, not enough disposable cups!")
            print()

    actions(water, milk, coffee_beans, disposable_cups, money)



def take (water, milk, coffee_beans, disposable_cups, money):
    print("I gave you $" + str(money))
    money = 0
    print()
    actions(water, milk, coffee_beans, disposable_cups, money)


def fill(water, milk, coffee_beans, disposable_cups, money):
    print()
    print("Write how many ml of water do you want to add:")
    water_inp = int(input())
    water += water_inp
    print("Write how many ml of milk do you want to add:")
    milk_inp = int(input())
    milk += milk_inp
    print("Write how many grams of coffee beans do you want to add:")
    coffee_beans_inp = int(input())
    coffee_beans += coffee_beans_inp
    print("Write how many disposable cups of coffee do you want to add:")
    disposable_cups_inp = int(input())
    disposable_cups += disposable_cups_inp
    print()
    actions(water, milk, coffee_beans, disposable_cups, money)


actions(water, milk, coffee_beans, disposable_cups, money)

exit()
