
import random

MAX_LINES = 3  # global constant
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbolCount = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

# spin slot


def spinSlot(rows, cols, sym):
    allSymbols = []  # an empty list
    for symbol, symbolCount in sym.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)
    columns = []
    for col in range(cols):
        for row in range(rows):
            value = random.choice(allSymbols)


# getting deposit

def deposit():
    while True:
        amount = input("Please deposit $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter a number")
    return amount

# getting number of bet lines


def numberOfLines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Please enter a number")
    return lines

# getting bet amount


def getBet():
    while True:
        bet = input("What would you like to bet on ebach line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET}-${MAX_BET}")
        else:
            print("Please enter a number")
    return bet

# the main function


def main():
    balance = deposit()
    lines = numberOfLines()
    while True:
        bet = getBet()
        totalBet = bet * lines
        if totalBet > balance:
            print(
                f"You do not have enough amount. Your current balance is ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Your total bet is ${totalBet}")


main()
