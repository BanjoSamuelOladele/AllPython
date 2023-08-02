from tictactoe.Board import Board
from tictactoe.Game import Game

__game_boy = Game()
board = Board()


def main():
    __game_boy.start_game()
    board.showBoard()


if __name__ == "__main__":
    main()
