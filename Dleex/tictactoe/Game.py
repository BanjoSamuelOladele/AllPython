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
            self.__player_one.setName(input(f"Enter player {number + 1} name: "))
            self.__player_one.setSign(input(f"Enter player {number + 1} icon: "))
            print()

        if number == 1:
            self.__player_two.setName(input(f"Enter player {number + 1} name: "))
            self.__player_two.setSign(input(f"Enter player{number + 1} icon: "))


