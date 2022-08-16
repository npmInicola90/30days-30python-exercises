mport random

def roll_dice():
    return random.randint(1,6)

def main():
    print("Welcome to the betting machine")
    print("You have $100 to start with")
    money = 100
    while money > 0:
        print("You have $" + str(money) + " left")
        bet = int(input("How much would you like to bet? "))
        if bet > money:
            print("You don't have that much money")
            continue
        dice1 = roll_dice()
        dice2 = roll_dice()
        print("You rolled a " + str(dice1) + " and a " + str(dice2))
        if dice1 == dice2:
            money += bet
            print("You win!")
        else:
            money -= bet
            print("You lose!")
    print("You are out of money!")

main()
