class Board:
    __running_game = True
    __winner = None
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

    def clear_board(self):
        self.__element_position.clear()

    def play_game(self, number: int, player: str):
        self.assign_player_choice(number, player)
        print(self.showBoard())
        print(self.check_running_game(self.__element_position))
        self.__winner = player
        return self.__winner

    def assign_player_choice(self, element_number: int, player):
        if self.__element_position[element_number] == " ":
            self.__element_position[element_number] = player
        else:
            raise ValueError("Already filled, pick another position")

    # for game in action
    def check_running_game(self, board: list):
        self.__check_if_win(board)
        self.__check_if_tie(board)

    # for continuity of game
    def ask_for_continuity(self, status: bool):
        self.__running_game = status

    def sort_game_status(self) -> bool:
        return self.__running_game

    def __check_if_win(self, board: list) -> str:
        if (self.__check_for_row(board) or
                self.__check_horizontally(board) or
                self.__check_diagonal(board)):
            self.__running_game = False
            return "It is a win"

    def __check_for_row(self, board: list):
        if board[1] == board[2] == board[3]:
            return True
        elif board[4] == board[5] == board[6]:
            return True
        elif board[7] == board[8] == board[9]:
            return True

    def __check_horizontally(self, board: list):
        if board[1] == board[4] == board[7]:
            return True
        elif board[2] == board[5] == board[8]:
            return True
        elif board[3] == board[6] == board[9]:
            return True

    def __check_diagonal(self, board: list):
        if board[1] == board[5] == board[9]:
            return True
        elif board[3] == board[5] == board[7]:
            return True

    def __check_if_tie(self, board: list):
        if " " not in board:
            return "It is a tie"
        self.__running_game = False
