import uuid


class Account:
    def __init__(self):
        self.balance = 0
        self.transactions = []
        print('\n'.join(self.transactions))


    def display_account(self):
        print(f"Account Balance: ${self.balance}")
        print("______________________")

    def deposit(self, amount):
        if amount > 0:
            transaction_id = str(uuid.uuid4())  # Generate a unique transaction ID
            self.balance += amount
            self.transactions.append(f"\nTransaction ID: {transaction_id}, Deposited ${amount}")
            print(f"\nAmount: {amount} deposited successfully\nNew Balance: {self.balance}")
            print("______________________")


    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            transaction_id = str(uuid.uuid4())  # Generate a unique transaction ID
            self.balance -= amount
            self.transactions.append(f"\nTransaction ID: {transaction_id}, Withdrawn ${amount}")
            print(f"\nAmount: {amount} Withdrawed successfully\nNew Balance: {self.balance}")
            print("______________________")
            return True
        else:
            print("Invalid amount or insufficient balance. Withdrawal denied.")
            return False

    def transfer(self, recipient_account, amount):
        if amount > 0 and self.balance >= amount:
            transaction_id = str(uuid.uuid4())  # Generate a unique transaction ID
            self.balance -= amount
            recipient_account.balance += amount
            self.recipient_account = recipient_account
            self.transactions.append(f"\nTransaction ID: {transaction_id}, Transferred ${amount} to {recipient_account}")
            print(f"\nAmount: {amount} Transfered successfully into Account: {self.recipient_account}\nNew Balance: {self.balance}")
            print("______________________")
            return True
        else:
            print("Invalid amount or insufficient balance. Transfer denied.")
            print("______________________")
            return False

    def display_transactions(self):
        if not self.transactions:
            print("No Previous Transactions to show.")
            print("______________________")
        else:
            for transaction in self.transactions:
                print(transaction)