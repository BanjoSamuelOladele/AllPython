from typing import Any

from Bank import Account


class Bank:
    # __count = 0
    # __accounts = list[Account]

    def __init__(self):
        self.__accounts = []

    def register_new_customer(self, first_name: str, last_name: str, password: str):
        account_number = "2233445566" + str(self.__accounts.__len__())
        account = Account.Accounts(first_name, last_name, password)
        account.set_account(account_number)
        print(account_number)
        self.__accounts.append(account)

    def size(self):
        print("size is ", self.__accounts.__len__())
        return self.__accounts.__len__()

    # def get_account(self, account_number):
    #     return self.accounts.get(account_number)

    def deposit_to_account(self, account_number, amount):
        for account in self.__accounts:
            if account.get_account(self) == account_number:
                account.deposit(self, amount)

    def check_balance_via_account(self, account_number, pin):
        for account in self.__accounts:
            print("acounting ", account)
            if account.get_account() == account_number:
                print("account is", account.get_account())
                print("acct ", account_number)
                account.deposit(pin)
        # account = self.find_account_by_account_number(account_number)
        # account.check_balance(pin)

    def __find_account_by_account_number(self, account_number) -> Account.Accounts:
        for account in self.__accounts:
            if account.get_account() == account_number:
                return account
