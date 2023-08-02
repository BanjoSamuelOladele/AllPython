import re


class Player:
    def __init__(self):
        self.__sign = None
        self.__name = None

    def setName(self, name: str):
        if name.isalpha():
            self.__name = name
        else:
            raise ValueError("Only alphabet")

    def setSign(self, sign: str):
        if sign.isalpha():
            self.__sign = sign
        else:
            raise ValueError("Use only Alphabets")

    def getName(self):
        return self.__name

    def getSign(self):
        return self.__sign

    def movePlayer(self):
        inp = input("Enter a position: ")
        if inp.isdigit():
            if 1 <= int(inp) <= 9:
                return inp
            else:
                print("input must be between 1 - 9")
                self.movePlayer()
        else:
            print("Input must be digit")
            self.movePlayer()
