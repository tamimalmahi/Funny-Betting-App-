import os
import time
import random

def balance(amount):
    if amount > 0:
        print(f"Available Balance: {amount}")
    elif amount == 0:
        print("Applicable for loan")
        print(f"Available Balance: {amount}")
    else:
        print("Loan Applied")
        print(f"Balance: {amount}")

def diposit(amount):
    os.system('cls')
    diposit = int(input("Enter amount of diposit: "))
    amount = amount + diposit
    print(f"Diposit successfull! Corrent Balance: {amount}")
    backMainManu(amount, loss)
    return amount

def backMainManu(amount, loss):
    choice = int(input("Press 1 to go back: "))

    if choice == 1:
        mainInterface(amount, loss)

def withdraw(amount, loss):
    os.system('cls')
    balance(amount)
    withdraw = int(input("Enter the amount you want to withraw: "))

    if amount < 500:
        print("You must have balance = 500, to withdraw!!")
        backMainManu(amount, loss)
    elif amount <= withdraw+100:
        print("You can't withdraw now!")
        backMainManu(amount, loss)
    else:
        amount = amount - withdraw
        print(f"Payment of {withdraw}$ has been successfull")
        print(f"Current Balance: {amount}")
        backMainManu(amount, loss)
        return amount
    
def mainJua(amount, loss):
    os.system('cls')
    if amount == 0:
        print("Sala fokinni Age tk vor tarpor jua khelte ay")
        backMainManu(amount, loss)
    else:
        print("Cholen hoye jak")
        actGame(amount, loss)

def playAgain(amount, loss):
    choice = int(input("Press 1 to play again, 2 for Back to the main manu: "))

    if choice == 1:
        actGame(amount, loss)
    elif choice == 2:
        mainInterface(amount, loss)

# def loose(amount, bet):
#     amount = amount - bet
#     return amount

# def win(amount, bet):
#     amount = amount + bet
#     return amount

def actGame(amount, loss):
    os.system('cls')
    print(f"Available Balance: {amount}")
    bet = int(input("Enter betting amount: "))

    a = random.randrange(1,4)
    b = random.randrange(1,4)
    c = random.randrange(1,4)
    nums = [a, b, c]

    for number in nums:
       print(number, end=" ", flush=True)
       time.sleep(0.3)
    
    if (a == b != c) or (a != b != c):
        print("Win Forward!!\t\tToo close for JACKPOT")
        amount = amount - (bet * 0.2)
        print(f"Loss: {bet * 0.2}")
        loss = loss + (bet * 0.2)
        playAgain(amount, loss)
    elif a != b == c:
        print("Win Backward!!\t\tToo close for JACKPOT")
        amount = amount - (bet * 0.2)
        print(f"Loss: {bet * 0.2}")
        loss = loss + (bet * 0.2)
        playAgain(amount, loss)
    elif a != b != c:
        print("Badluck this time!!!")
        print(f"Loss: {bet}")
        loss = loss + (bet)
        amount = amount - bet
        playAgain(amount, loss)
    elif a == b == c:
       print()
       print("\t\t\t\tBIG WIN!!")
       print("\t\t\t\tJACKPOOOOT")
       amount = amount + (bet * 20)
       loss = loss - (bet * 20)
       playAgain(amount, loss)

def balInq(loss):
    print(f"Total loss: {loss}")

# def login():
#     userName = "admin"
#     userPass = "admin"
#     adminName = "amirealadmin"
#     adminPass = "khuljasimsim"
#     print("Enter username as 'admin' for QuickPlay!")
#     tempName = input("Enter username @")
#     print("Enter password as 'admin' for QuickPlay!")
#     tempPass = input("Enter password: ")

#     if tempName == userName and tempPass == userPass:
#         user = 1
#         return user
#     elif tempName == adminName and tempPass == adminPass:
#         user = 2
#         return user

def mainInterface(amount, loss):
    os.system('cls')
    balance(amount)
    print("JUARI.ADDA")
    print("1. Go RICH🤑")
    print("2. Diposit")
    print("3. Withdraw")
    print("4. Balance Inquary")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        mainJua(amount, loss)

    elif choice == 2:
        diposit(amount)

    elif choice == 3:
        withdraw(amount)
    elif choice == 4:
        balInq(loss)

loss = 0
amount = 0
mainInterface(amount, loss)