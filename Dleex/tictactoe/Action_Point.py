class Action_Entity:
    __running_game = True

    def get_game_status(self):
        return self.__running_game

    def check_running_game(self, board: list):
        self.__check_if_win(board)
        self.__check_if_tie(board)

    def __check_if_win(self, board: list) -> str:
        if self.__check_for_row(board) or self.__check_horizontally(board) or self.__check_diagonal(
                board):
            self.__running_game = False
            return "It is a win"

    def __check_for_row(self, board: list) -> bool:
        if board[1] == board[2] == board[3]:
            return True
        elif board[4] == board[5] == board[6]:
            return True
        elif board[7] == board[8] == board[9]:
            return True

    def __check_horizontally(self, board: list) -> bool:
        if board[1] == board[4] == board[7]:
            return True
        elif board[2] == board[5] == board[8]:
            return True
        elif board[3] == board[6] == board[9]:
            return True

    def __check_diagonal(self, board: list) -> bool:
        if board[1] == board[5] == board[9]:
            return True
        elif board[3] == board[5] == board[7]:
            return True

    def __check_if_tie(self, board: list) -> str:
        if " " not in board:
            self.__running_game = False
            return "It is a tie"
