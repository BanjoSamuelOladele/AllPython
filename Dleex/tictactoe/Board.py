from Dleex.tictactoe.Action_Point import Action_Entity


class Board:
    __running_game = True
    __winner = None
    __action_ = Action_Entity()
    __element_position = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def showBoard(self):
        formatted_string = "{} | {} | {} \n" \
                           "-----------\n" \
                           "{} | {} | {} \n" \
                           "-----------\n" \
                           "{} | {} | {} ".format(self.__element_position[1], self.__element_position[2],
                                                  self.__element_position[3], self.__element_position[4],
                                                  self.__element_position[5], self.__element_position[6],
                                                  self.__element_position[7], self.__element_position[8],
                                                  self.__element_position[9])
        print(formatted_string)

    def play_game(self, number: int, player: str):
        self.assign_player_choice(number, player)
        print(self.showBoard())
        self.check_running_game(self.__element_position)
        if not self.__running_game:
            print(self.__get_winner(), "won")

    def __get_winner(self):
        return self.__winner

    def assign_player_choice(self, element_number: int, player):
        if self.__element_position[element_number] == " ":
            self.__element_position[element_number] = player
        else:
            raise ValueError("Already filled, pick another position")

    # for game in action
    def check_running_game(self, board: list):
        self.__running_game = self.__action_.check_for_win(board)
        return self.__running_game

    # for continuity of game
    def sort_game_status(self) -> bool:
        return self.__running_game
