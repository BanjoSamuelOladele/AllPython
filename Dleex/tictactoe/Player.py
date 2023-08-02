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

    def getSign(self) -> str:
        return self.__sign

    def move_player(self):
        inp = input("Enter a position between 1 - 9: ")
        if inp.isdigit():
            if 1 <= int(inp) <= 9:
                return int(inp)
            else:
                raise ValueError("input must be between 1 - 9")
        else:
            raise ValueError("Must be digit alone")
