class Account:
    def __init__(self, first_name, last_name, password):
        self.__account_number = None
        self.__amount = 0
        self.__first_name = first_name
        self.__last_name = last_name
        self.__password = password

    def deposit(self, amount):
        if amount > 0:
            self.__amount += amount

    def check_balance(self, password: str):
        if self.__password == password:
            return self.__amount
        return 0

    def withdraw(self, pin: str, amount: float):
        if self.__password == pin:
            if amount > 0:
                self.__amount -= amount

    def set_account(self, account_number):
        self.__account_number = account_number

    def get_account(self):
        return self.__account_number
