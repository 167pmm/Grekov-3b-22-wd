import time


def exist_client(k, obj):
    return k in obj


class BankClient:
    def __init__(self, name, surname):
        self.client_id = str(name) + str(surname) + str(time.time())
        self.name = name
        self.surname = surname
        self.accounts = {}

    def create_account(self, account_type, amount):
        self.accounts[account_type] = {
            "amount": amount
        }

    def check_exit_and_balance_enough(self, account_type, amount):
        return bool(self.accounts[account_type]) & bool(self.accounts[account_type]["amount"] >= amount)

    def change_balance(self, account_type, summ, operation_type):
        if operation_type == 'plus':
            self.accounts[account_type]["amount"] += summ

        if operation_type == 'minus':
            self.accounts[account_type]["amount"] -= summ


class Bank:
    def __init__(self):
        self.clients = {}
        self.transaction = []

    def create_client(self, name, surname):
        new_client = BankClient(name, surname)
        self.clients[new_client.client_id] = new_client

        return new_client

    def transfer(self, client_instance, transfer_from, transfer_to, summ):
        client = self.clients[client_instance.client_id]

        if client.check_exit_and_balance_enough(transfer_from, summ) & client.check_exit_and_balance_enough(transfer_to, 0):
            client.change_balance(transfer_from, summ, 'minus')
            client.change_balance(transfer_to, summ, 'plus')

            self.transaction.append({
                'client_instance': client_instance,
                'transfer_from': transfer_from,
                'transfer_to': transfer_to,
                'time': time.time(),
                'summ': summ
            })
        else:
            print('Ошибка при осущевлении операции перевода')


test_bank = Bank()
happy_client = test_bank.create_client('Victor', 'Test')
happy_client.create_account('debit', 50000)
happy_client.create_account('credit', 0)

test_bank.transfer(happy_client, 'debit', 'credit', 5000)

print("debit is 45000? " + str(happy_client.accounts["debit"]["amount"] == 45000))
print("credit is 5000? " + str(happy_client.accounts["credit"]["amount"] == 5000))
