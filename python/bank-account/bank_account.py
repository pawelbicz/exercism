class BankAccount(object):
    def __init__(self):
        self.balance = 0
        self.is_open_account = False

    def get_balance(self):
        if self.is_open_account:
            return self.balance
        else:
            raise ValueError('Account not created or closed')

    def open(self):
        self.is_open_account = True

    def deposit(self, amount):
        if self.is_open_account and amount > 0:
            self.balance += amount
        else:
            raise ValueError('Account not created or closed')

    def withdraw(self, amount):
        if self.is_open_account and self.balance >= amount and amount > 0:
            self.balance -= amount
        else:
            raise ValueError('Account not created or closed')

    def close(self):
        self.is_open_account = False

