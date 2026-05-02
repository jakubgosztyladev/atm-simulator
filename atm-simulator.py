user_pin = '0055'
account_balance = 1000
euro_exchange_rate = 4.7

login_attempts = 3
entered_pin = input("Enter your PIN: ")

while login_attempts > 1 or entered_pin == user_pin:
    if entered_pin == user_pin:
        while True:
            print("-----MENU-----")
            print("1. Check account balance")
            print("2. Deposit funds")
            print("3. Withdraw funds")
            print("4. Check account balance in EURO")
            print("5. Exit")
            x = int(input("Select option: "))
            if x == 1:
                print("Account balance: ", account_balance, "PLN")
                continue
            elif x == 2:
                deposit_amount = float(input("Enter the amount you want to deposit: "))
                if deposit_amount > 0:
                    account_balance += deposit_amount
                    print(f"Deposited {deposit_amount} PLN")
                else:
                    print("Invalid amount entered")
                    continue
            elif x == 3:
                withdrawal_amount = float(input("Enter the amount you want to withdraw: "))
                if withdrawal_amount > 0 and account_balance > 0 and withdrawal_amount <= account_balance:
                    account_balance -= withdrawal_amount
                    print(f"Withdrawn {withdrawal_amount} PLN")
                else:
                    print("Insufficient funds or invalid amount entered")
                    continue
            elif x == 4:
                print("Account balance in EURO: ", round(account_balance / euro_exchange_rate, 2), "EUR")
            elif x == 5:
                print("Thank you for using the ATM!")
                break
            else:
                print("Unrecognized operation. Please check the selected option.")
                continue
        break
    else:
        login_attempts -= 1
        entered_pin = input(f"Incorrect PIN! Remaining login attempts: {login_attempts}. Please enter your PIN again: ")