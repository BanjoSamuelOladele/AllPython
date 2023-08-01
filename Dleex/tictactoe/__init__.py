from tictactoe.Board import Board
from tictactoe.Player import Player

player = Player()
player2 = Player()
board = Board()


def main():
    print(board.showBoard())


#
# def main():
#     try:
#         player.setName(input("Enter player 1 name: "))
#         player.setSign(input("Enter player 1 sign: "))
#         player2.setName(input("Enter player 2 name: "))
#         try:
#             player2.setSign(input("Enter player 2 sign: "))
#             if player.getSign() == player2.getSign():
#                 raise ValueError("it has been taken by player 1")
#         except ValueError as error2:
#             print(error2)
#     except ValueError as error:
#         print(error)
#
#     print(player.getName(), "and sign is", player.getSign())
#     print(player2.getName(), "and sign is", player2.getSign())


if __name__ == "__main__":
    main()
