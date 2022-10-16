import datetime


class BankAccount:
    balance = 0
    transaction = []

    def __init__(self, name, uuid):
        self.name = name
        self.uuid = uuid

    def deposit_money(self, amount: int):
        self.balance += amount
        self.transaction.append('Deposit success. Current balance is ' + str(self.balance) +
                                'Date: ' + datetime.datetime.now().date())
        print("Operation success")

    def cash_out(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount * 1.01
            self.transaction.append('Cash out success. Bank fee is:' + str(amount * 0.01) +
                                    'Current balance is ' + str(self.balance) +
                                    'Date: ' + datetime.datetime.now().date())
            print('Operation success. Your current balance is ' + str(self.balance))
        else:
            self.transaction.append('Cash out failed. Not enough money.' +
                                    'Date: ' + datetime.datetime.now().date())
            print('Operation failed. Not enough money. Current balance is ' + str(self.balance))

    def balance_info(self):
        print('Balance = ' + str(self.balance))
