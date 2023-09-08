from user import User


class BankingSystem:
    def __init__(self):
        self.users = []

    def run(self):
        while True:
            print("\nBanking System Menu:")
            print("1. Create Account")
            print("2. Display Account")
            print("3. Deposit Cash")
            print("4. Withdraw Cash")
            print("5. Transfer Cash")
            print("6. Transaction History")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_account()

            elif choice == '2':
                self.display_account()

            elif choice == '3':
                self.deposit_cash()

            elif choice == '4':
                self.withdraw_cash()

            elif choice == '5':
                self.transfer_cash()

            elif choice == '6':
                self.transaction_history_specific()

            elif choice == '7':
                print("**************************\nExiting the banking system. Goodbye!\n**************************")
                break

            else:
                print("Invalid choice. Please try again.")

    def create_account(self):
        username = input("Enter a username (must be unique): ")

        # Check if username already exists
        if any(user.username == username for user in self.users):
            print("Username already exists. Please choose another.")
            print("______________________")
            return

        pin = input("Set a PIN: ")
        user = User(username, pin)
        self.users.append(user)
        print(f"Account created successfully! Your unique account number is: '{user.account_number}'")
        print("______________________")

    def display_account(self):
        username = input("Enter your username: ")
        user = next((u for u in self.users if u.username == username), None)
        if user:
            user.display_account()
        else:
            print("User not found!")
            print("______________________")

    def deposit_cash(self):
        username = input("Enter your username: ")
        user = next((u for u in self.users if u.username == username), None)
        if user:
            user.deposit_cash()
        else:
            print("User not found!")
            print("______________________")

    def withdraw_cash(self):
        username = input("Enter your username: ")
        user = next((u for u in self.users if u.username == username), None)
        if user:
            user.withdraw_cash()
        else:
            print("User not found!")
            print("______________________")

    def transfer_cash(self):
        sender_username = input("Enter your username: ")
        sender = next((u for u in self.users if u.username == sender_username), None)
        if sender:
            recipient_username = input("Enter recipient's username: ")
            recipient = next((u for u in self.users if u.username == recipient_username), None)
            if recipient:
                sender.transfer_cash(recipient)
            else:
                print("Recipient not found!")
                print("______________________")
        else:
            print("Sender not found!")
            print("______________________")

    def transaction_history_specific(self):
        username = input("Enter your username: ")
        user = next((u for u in self.users if u.username == username), None)
        if user:
            user.transaction_history()

    