from Dleex.tictactoe import Board
from Dleex.tictactoe import Player


class Game:
    __player_one = Player.Player()
    __player_two = Player.Player()
    __board = Board.Board()

    def start_game(self):
        print("Tic Tac Toe")
        self.__create_player()
        print("Player 1 Name = ", self.__player_one.getName(),
              "Icon is", self.__player_one.getSign())
        print("Player 2 Name = ", self.__player_two.getName(),
              "Icon is", self.__player_two.getSign())
        self.__run_game()

    def __create_player(self):
        for number in range(0, 2):
            self.__call_class_player(number)

    def __run_game(self):
        print(self.__board.showBoard())
        for num in range(0, 9):
            while self.__board.sort_game_status():
                self.__extracts(num)
        print("bye bye")

    def __extracts(self, num):
        if num % 2 == 0:
            number = 0
            try:
                number = self.__player_one.move_player(self.__player_one.getSign())
                self.__play_with(number, self.__player_one.getSign())
                num += 1
            except ValueError as error:
                print(error)
                self.__play_with(number, self.__player_one.getSign())
        if num % 2 != 0:
            number = 0
            try:
                number = self.__player_two.move_player(self.__player_two.getSign())
                self.__play_with(number, self.__player_two.getSign())
                num += 1
            except ValueError as err:
                print(err)
                self.__play_with(number, self.__player_two.getSign())

    def __play_with(self, number, player):
        self.__board.play_game(number, player)

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
        self.__checking_player_index(number, sign)

    def __checking_player_index(self, number, sign):
        if number == 0:
            self.__player_one.setSign(sign)
        if number == 1:
            check = self.__player_one.getSign().lower()
            if check != sign.lower():
                self.__player_two.setSign(sign)
            else:
                print(sign, "already taken")
                self.__create_player_sign(number)
