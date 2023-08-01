class Board:
    __running_game = True
    __winner = None
    __element_position = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def showBoard(self):

        # print("__________")
        # print("%s | %s | %s" % (self.__element_position[1], self.__element_position[2], self.__element_position[3]))
        # print("__________")
        # print(self.__element_position[4], "|", self.__element_position[5], "|", self.__element_position[6])
        # print("__________")
        # print(self.__element_position[7], "|", self.__element_position[8], "|", self.__element_position[9])
        # print("__________")

    def playGame(self):
        self.showBoard()

    def assignPlayerChoice(self, element_number, player):
        self.__element_position[element_number] = player

    def shifting(self):
        position = int(input("Enter 1 - 9: ")) - 1

        self.__element_position[position] = "X"

    def check_running_game(self, board: list):
        self.__check_if_win(board)
        self.__check_if_tie(board)

    def sort_game_status(self, status):
        self.__running_game = status

    def __check_if_win(self, board: list):
        if self.__check_for_row(board) or self.__check_horizontally(board) or self.__check_diagonal(board):
            return "It is a win"
        self.__running_game = False

    def __check_for_row(self, board: list):
        if board[0] == board[1] == board[2] and board[1] != " ":
            return True
        elif board[3] == board[4] == board[5] and board[4] != " ":
            return True
        elif board[6] == board[7] == board[8] and board[6] != " ":
            return True

    def __check_horizontally(self, board: list):
        if board[0] == board[3] == board[6] and board[0] != " ":
            return True
        elif board[1] == board[4] == board[7] and board[1] != " ":
            return True
        elif board[2] == board[5] == board[8] and board[6] != " ":
            return True

    def __check_diagonal(self, board: list):
        if board[0] == board[4] == board[8] and board[0] != " ":
            return True
        elif board[2] == board[4] == board[6] and board[4] != " ":
            return True

    def __check_if_tie(self, board: list):
        if " " not in board:
            return "It is a tie"
        self.__running_game = False
