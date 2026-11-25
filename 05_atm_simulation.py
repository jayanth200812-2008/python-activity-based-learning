# Case Study 5: ATM Transaction Sequence Simulation
balance = float(input("Enter opening balance: "))
transactions = []
while True:
    print("\n1.Deposit  2.Withdraw  3.Balance  4.Exit")
    choice = int(input("Choose: "))
    if choice == 1:
        amount = float(input("Deposit amount: "))
        if amount > 0:
            balance = balance + amount
            transactions.append(("Deposit", amount))
            print("Deposit successful")
        else:
            print("Invalid amount")
    elif choice == 2:
        amount = float(input("Withdrawal amount: "))
        if amount <= 0:
            print("Invalid amount")
        elif amount > 10000:
            print("Daily transaction limit exceeded")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance = balance - amount
            transactions.append(("Withdrawal", amount))
            print("Withdrawal successful")
    elif choice == 3:
        print("Balance: Rs.", round(balance, 2))
    elif choice == 4:
        break
    else:
        print("Invalid choice")

print("Transaction summary:")
for item in transactions:
    kind, amount = item
    print(kind, ": Rs.", amount)
print("Closing balance: Rs.", round(balance, 2))
