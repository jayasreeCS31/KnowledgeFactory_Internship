class Bank:
    def __init__(self):
        self.__balance = 5000
    def deposit(self, amount):
        self.__balance += amount
    def show_balance(self):
        print("Balance:", self.__balance)
b1 = Bank()
b1.deposit(2000)
b1.show_balance()