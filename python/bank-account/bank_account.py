from threading import Lock


class BankAccount(object):
    """ The BankAccount object contain information about client bank account """
    def __init__(self):
        self._balance = 0
        self._is_open_account = False
        self._lock = Lock()

    def get_balance(self):
        """ Return cash on account """
        with self._lock:
            if self._is_open_account:
                return self._balance
            else:
                raise ValueError('Account not created or closed')

    def open(self):
        """
        Opening new account

        :raise ValueError: Account already opened
        """
        with self._lock:
            if self._is_open_account is False:
                self._is_open_account = True
            else:
                raise ValueError('Account opened')

    def deposit(self, amount):
        """
        Deposit some money to an account

        :param amount: The amount of deposited cash
        :raise ValueError: Account is closed or amount of deposited cash <= 0
            """
        with self._lock:
            if self._is_open_account and amount > 0:
                self._balance += amount
            else:
                raise ValueError('Account not created or closed')

    def withdraw(self, amount):
        """
        Withdraw from an account

        :param amount: The amount of deposited cash
        :raise ValueError: Account is closed
                            or amount of withdrawed cash is bigger than in account
                            or amount of withdrawed cash <= 0
        """
        with self._lock:
            if self._is_open_account and self._balance >= amount and amount > 0:
                self._balance -= amount
            else:
                raise ValueError('Account not created or closed')

    def close(self):
        """
        Close bank account

        :raise ValuError: Account already closed
        """
        with self._lock:
            if self._is_open_account is True:
                self._is_open_account = False
                self._balance = 0
            else:
                raise ValueError('Account already closed')
