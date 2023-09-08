import random
from account import Account



class User:
    def __init__(self, username, pin):
        self.username = username
        self.pin = pin
        self.account = Account()
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        return random.randint(100000, 999999)

    def verify_pin(self, pin_to_check):
        if pin_to_check == self.pin:
            return True
        else:
            print("Incorrect PIN. Access denied.")
            return False

    def display_account(self):
        pin = input("Enter your PIN: ")
        if self.verify_pin(pin):
            print(f"\nAccount Number: {self.account_number}\nAccount Name: {self.username}")
            self.account.display_account()

    def deposit_cash(self):
        pin = input("Enter your PIN: ")
        if self.verify_pin(pin):
            amount = float(input("Enter the amount to deposit: "))
            self.account.deposit(amount)

    def withdraw_cash(self):
        pin = input("Enter your PIN: ")
        if self.verify_pin(pin):
            amount = float(input("Enter the amount to withdraw: "))
            self.account.withdraw(amount)

    def transfer_cash(self, recipient):
        pin = input("Enter your PIN: ")
        if self.verify_pin(pin):
            if recipient != self:
                amount = float(input("Enter the amount to transfer: "))
                self.account.transfer(recipient.account, amount)
            else:
                print("You cannot transfer money to your own account.")

    def transaction_history(self):
        pin = input("Enter your PIN: ")
        if self.verify_pin(pin):
            self.account.display_transactions()