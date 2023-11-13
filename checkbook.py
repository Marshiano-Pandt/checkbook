import os

# Define the filename for the ledger file
ledger_file = "atm_file.txt"

# Initialize the ledger if it doesn't exist
if not os.path.exists(ledger_file):
    with open(ledger_file, "w") as file:
        file.write("0.00")
def get_balance():
    with open(ledger_file, "r") as file:
        balance = float(file.read())
    return balance

def record_debit(amount):
    balance = get_balance()
    with open(ledger_file, "a") as file:
        file.write(f"Debit: ${amount:.2f}\n")
    update_balance(balance - amount)

def record_credit(amount):
    balance = get_balance()
    with open(ledger_file, "a") as file:
        file.write(f"Credit: ${amount:.2f}\n")
    update_balance(balance + amount)

def update_balance(new_balance):
    with open(ledger_file, "w") as file:
        file.write(f"{new_balance:.2f}")

def main():
    print("~~~ Welcome to your terminal checkbook! ~~~")

    while True:
        print("\nWhat would you like to do?")
        print("1) View current balance")
        print("2) Record a debit (withdraw)")
        print("3) Record a credit (deposit)")
        print("4) Exit")

        choice = input("Your choice? ")

        if choice == "1":
            balance = get_balance()
            print(f"Your current balance is ${balance:.2f}")

        elif choice == "2":
            while True:
                try:
                    amount = float(input("How much is the debit? $"))
                    record_debit(amount)
                    print("Debit recorded.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        elif choice == "3":
            while True:
                try:
                    amount = float(input("How much is the credit? $"))
                    record_credit(amount)
                    print("Credit recorded.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        elif choice == "4":
            print("Thanks, have a great day!")
            break

        else:
            print("Invalid choice:", choice)

if __name__ == "__main__":
    main()

