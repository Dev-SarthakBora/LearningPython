# encapsulation.py
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    # getter method
    def get_balance(self):
        return self.__balance

    # setter method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
# print(account.__balance)  # ❌ Error: can't access private attribute

