import re


class Player:
    def __init__(self):
        self.__sign = None
        self.__name = None

    # def __int__(self, name, sign):
    #     self.setName(name)
    #     self.setSign(sign)

    def setName(self, name):
        check = self.__contain_only_string(name)
        if check:
            self.__name = name
        else:
            print(ValueError("Only Alphabets allowed"))
            self.setName(name)

    def __contain_only_string(self, string_input: str) -> bool:
        pattern = r'^[a-zA-Z]+$'
        match = re.match(pattern, string_input)
        return bool(match)

    def setSign(self, sign):
        check = self.__contain_only_string(sign)
        if check:
            self.__sign = sign
        else:
            print(ValueError("Use only Alphabets"))
            self.setSign(sign)

    def getName(self):
        return self.__name

    def getSign(self):
        return self.__sign

    def movePlayer(self):
        try:
            return int(input("Enter a position: "))
        except TypeError as error:
            print("Not a number ", error)
            self.movePlayer()

# def main():
#     print(player.getName(), player.getSign())


# if __name__ == "__main__":
#     main()
