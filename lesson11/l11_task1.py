import BankAccount

bank = BankAccount.BankAccount('Alex', '12341')
bank.balance_info()
bank.deposit_money(10000)
bank.balance_info()
bank.cash_out(5000)
bank.balance_info()
bank.cash_out(120000)
print(bank.transaction)
