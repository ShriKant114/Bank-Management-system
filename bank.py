class BankAccount:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. Current balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

    def display_details(self):
        print(f"Account Holder: {self.name}, Account Number: {self.account_number}, Balance: ₹{self.balance}")


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, account_number):
        if account_number in self.accounts:
            print("❌ Account already exists.")
        else:
            self.accounts[account_number] = BankAccount(name, account_number)
            print(f"✅ Account created successfully for {name}.")

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("✅ Account deleted successfully.")
        else:
            print("❌ Account not found.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def view_all_accounts(self):
        if not self.accounts:
            print("⚠️ No accounts available.")
        else:
            print("\n--- All Bank Accounts ---")
            for account in self.accounts.values():
                account.display_details()


class AdminPanel:
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "12345"

    @staticmethod
    def login():
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")

        if username == AdminPanel.ADMIN_USERNAME and password == AdminPanel.ADMIN_PASSWORD:
            print("✅ Admin login successful.")
            return True
        else:
            print("❌ Incorrect username or password. Access denied.")
            return False


# ===== CLI Menu =====
bank = BankSystem()

while True:
    print("\n=== BANK MANAGEMENT SYSTEM ===")
    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Delete Account")
    print("6. Admin Panel (View All Accounts)")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == '1':
        name = input("Enter user name: ")
        acc_no = input("Enter account number: ")
        bank.create_account(name, acc_no)

    elif choice == '2':
        acc_no = input("Enter account number: ")
        acc = bank.get_account(acc_no)
        if acc:
            amount = float(input("Enter amount to deposit: "))
            acc.deposit(amount)
        else:
            print("❌ Account not found.")

    elif choice == '3':
        acc_no = input("Enter account number: ")
        acc = bank.get_account(acc_no)
        if acc:
            amount = float(input("Enter amount to withdraw: "))
            acc.withdraw(amount)
        else:
            print("❌ Account not found.")

    elif choice == '4':
        acc_no = input("Enter account number: ")
        acc = bank.get_account(acc_no)
        if acc:
            acc.check_balance()
        else:
            print("❌ Account not found.")

    elif choice == '5':
        acc_no = input("Enter account number to delete: ")
        bank.delete_account(acc_no)

    elif choice == '6':
        if AdminPanel.login():
            bank.view_all_accounts()

    elif choice == '7':
        print("👋 Thank you for using the bank management system. Goodbye!")
        break

    else:
        print("⚠️ Invalid option. Please choose between 1-7.")
