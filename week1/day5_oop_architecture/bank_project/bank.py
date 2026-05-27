balance = 1000
def check_balance():
    return balance
def deposit(amount):
    global balance
    balance = balance + amount
    return balance
def withdraw(amount):
    global balance
    if amount <= balance:
        balance = balance - amount
        return "Withdrawal Successful"
    else:
        return "Insufficient Balance"