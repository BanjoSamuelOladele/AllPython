"""Create a class account and it instances"""
from decimal import Decimal


class Account:
    def __init__(self, name: str, balance: Decimal, age: int):
        self.name = name
        self.balance = balance
        self.age = age

    def __str__(self):
        return f"{self.name} {self.balance} {self.age}"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            return ValueError("Below zero")
        self.__balance = amount

    @property
    def username(self):
        return self.__name

    @username.setter
    def username(self, name):
        self.__name = name

    def withdraw(self, amount):
        if amount > self.__balance:
            return ValueError("scam")
        self.__balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            return ValueError("scam")


account1 = Account("Dele", Decimal(100.00), 18)

from account import Decimal

# print(account1)
