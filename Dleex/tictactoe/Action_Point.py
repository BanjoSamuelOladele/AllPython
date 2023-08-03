class Action_Entity:

    def check_for_tie(self, inp: list):
        if " " not in inp:
            print(inp)
            print("it is a tie")
            return False

    def __check_for_row(self, inp: list):
        if inp[1] == inp[2] == inp[3] and inp[1] != " ":
            return True
        elif inp[4] == inp[5] == inp[6] and inp[4] != " ":
            return True
        elif inp[7] == inp[8] == inp[9] and inp[7] != " ":
            return True

    def __check_horizontally(self, inp: list):
        if inp[1] == inp[4] == inp[7] and inp[1] != " ":
            return True
        elif inp[2] == inp[5] == inp[8] and inp[2] != " ":
            return True
        elif inp[3] == inp[6] == inp[9] and inp[3] != " ":
            return True

    def __check_diagonal(self, inp: list):
        if inp[1] == inp[5] == inp[9] and inp[1] != " ":
            return True
        elif inp[3] == inp[5] == inp[7] and inp[3] != " ":
            return True

    def check_for_win(self, inp: list) -> bool:
        if self.__check_diagonal(inp) or self.__check_horizontally(inp) or self.__check_for_row(inp):
            print("it is a win!")
            return True
