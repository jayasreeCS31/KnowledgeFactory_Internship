from bank import deposit, withdraw, check_balance
while True:
    print("\n BANK MENU ")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Current Balance:", check_balance())
    elif choice == "2":
        amount = int(input("Enter deposit amount: "))
        print("Updated Balance:", deposit(amount))
    elif choice == "3":
        amount = int(input("Enter withdraw amount: "))
        print(withdraw(amount))
        print("Current Balance:", check_balance())
    elif choice == "4":
        print("Thank You")
        break
    else:
        print("Invalid Choice")