import re


def contain_only_string(string_input):
    pattern = r'^[a-zA-Z]+$'
    match = re.match(pattern, string_input)
    return bool(match)


class Player:
    def __init__(self):
        self.__sign = None
        self.__name = None

    def __int__(self, name, sign):
        self.setName(name)
        self.setSign(sign)

    def setName(self, name):
        check = contain_only_string(name)
        if check:
            self.__name = name
        else:
            raise ValueError("Only Alphabets allowed")

    def setSign(self, sign):
        check = contain_only_string(sign)
        if check:
            self.__sign = sign
        else:
            raise ValueError("Use only Alphabets")

    def getName(self):
        return self.__name

    def getSign(self):
        return self.__sign

    def movePlayer(self):
        int(input("Enter a position: "))


player = Player()
try:
    player.setName("Dele")
except ValueError as error:
    print(error)
try:
    player.setSign("4")
except ValueError as error:
    print(error)


def main():
    print(player.getName(), player.getSign())


if __name__ == "__main__":
    main()
