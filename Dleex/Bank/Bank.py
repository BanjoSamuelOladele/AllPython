from Bank import Account


class Bank:
    # __count = 0
    # # __accounts = list[Account.Account]
    __accounts = None

    def __init__(self):
        self.__count = 0
        self.__accounts = None
        self.__accounts = []

    def register_new_customer(self, first_name: str, last_name: str, password: str):
        account_number = "2233445566" + str(self.__count)
        account = Account.Account(first_name, last_name, password)
        account.set_account(account_number)
        self.__accounts.append(account)
        self.__count += 1

    def size(self):
        return self.__count

    @classmethod
    def deposit_to_account(cls, account_number, amount):
        account = Account.Account
        for account in cls.__accounts:
            if account == account_number:
                account.deposit(amount)

    def check_balance_via_account(self, account_number, pin):
        account = Account.Account
        account = self.find_account_by_account_number(account_number)
        account.check_balance(pin)

    def find_account_by_account_number(self, account_number: str) -> Account.Account:
        account = Account.Account
        for account in self.__accounts:
            if account.getAccountNumber() == account_number:
                return account
        return None
