
# this ammount

def deposit():
    while True:
        amount = input("Please deposit $ ")
        if amount.isdigit():
            amount = int(amount)