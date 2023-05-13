class BankAccount:

    def __init__(self, name, acc_number, balance):
        self.name = name
        self.acc_number = acc_number
        self.balance = balance

    def top_up(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

my_account = BankAccount("Герман", 4276400037914505, 32000000.00)

print(my_account.balance)
my_account.top_up(100000.00)
print(my_account.balance)
my_account.withdraw(200000.00)
print(my_account.balance)