from Dleex.tictactoe import Board
from Dleex.tictactoe import Player


class Game:
    __player_one = Player.Player()
    __player_two = Player.Player()
    __board = Board.Board()
    # def __int__(self):
    #     self.__player_one = Player.Player()
    #     self.__player_two = Player.Player()
    #     self.__board = Board.Board()

    def start_game(self):
        print("Tic Tac Toe")
        self.__create_player()
        print("Player 1 Name = ", self.__player_one.getName(), " ", self.__player_one.getSign())
        print("Player 2 Name = ", self.__player_two.getName(), " ", self.__player_two.getSign())
        self.__run_game()

    def __create_player(self):
        for number in range(0, 2):
            self.__call_class_player(number)

    def __run_game(self):
        print(self.__board.showBoard())
        while self.__board.sort_game_status():
            for num in range(0, 9):
                if num % 2 == 0:
                    try:
                        number = self.__player_one.move_player()
                        self.__board.play_game(number, self.__player_one.getSign())
                    except ValueError as error:
                        print(error)
                if num % 2 != 0:
                    try:
                        number = self.__player_two.move_player()
                        self.__board.play_game(number, self.__player_two.getSign())
                    except ValueError as err:
                        print(err)

        choice = input("would you like to continue? ")
        if choice.lower() == "y":
            self.__board.ask_for_continuity(True)
        else:
            print("bye bye")

    def __call_class_player(self, number: int):
        try:
            self.__create_player_name(number)
            print()
        except ValueError as error:
            print(error)

    def __create_player_name(self, index):
        name = None
        try:
            name = input(f"Enter player {index + 1} name: ")
            self.__create_player_sign(index)
        except ValueError as error:
            print(error)
            self.__create_player_name(index)
        if index == 0:
            self.__player_one.setName(name)
        if index == 1:
            self.__player_two.setName(name)

    def __create_player_sign(self, number):
        sign = None
        try:
            sign = input(f"Enter player{number + 1} icon: ")
        except ValueError as error:
            print(error)
            self.__create_player_sign(number)
        if number == 0:
            self.__player_one.setSign(sign)
        if number == 1:
            if self.__player_one.getSign() != sign:
                self.__player_two.setSign(sign)
            else:
                print(sign, "already taken")
                self.__create_player_sign(number)
