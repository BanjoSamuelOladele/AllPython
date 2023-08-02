from Dleex.tictactoe import Board
from Dleex.tictactoe.Player import Player


class Game:
    def __int__(self):
        self.__player_one = None
        self.__player_two = None
        self.__board = Board.Board

    def start_game(self):
        print("Tic Tac Toe")
        self.__create_player()
        self.__run_game()

    def __create_player(self):
        for number in range(0, 2):
            self.__call_class_player(number)

    def __run_game(self):
        print(self.__board.showBoard())

    def __call_class_player(self, number: int):
        self.__player_one = Player()
        self.__player_two = Player()
        if number == 0:
            try:
                self.__create_player_name(number, self.__player_one, self.__player_two)
                self.__create_player_sign(number, self.__player_one, self.__player_two)
                print()
            except ValueError as error:
                print(error)
        if number == 1:
            try:
                self.__create_player_name(number, self.__player_one, self.__player_two)
                self.__create_player_sign(number, self.__player_one, self.__player_two)
            except ValueError as error:
                print(error)

    def __create_player_name(self, index, play1:Player, play2:Player):
        name = None
        try:
            name = input(f"Enter player {index + 1} name: ")
        except ValueError as error:
            print(error)
            self.__create_player_name(index,play1,play2)
        if index == 0:
            play1.setName(name)
        if index == 1:
            play2.setName(name)

    def __create_player_sign(self, number, playe1: Player, play2: Player):
        sign = None
        try:
            sign = input(f"Enter player{number + 1} icon: ")
        except ValueError as error:
            print(error)
            self.__create_player_sign(number,playe1,play2)
        if number == 0:
            playe1.setSign(sign)
        if number == 1:
            play2.setSign(sign)
