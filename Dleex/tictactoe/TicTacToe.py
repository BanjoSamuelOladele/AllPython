board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

player1 = "xX"
player2 = "oO"
running_game = True


def printBoard(inp: list):
    print(f"{inp[0]}   | {inp[1]}   | {inp[2]}\n"
          f"---------------\n"
          f"{inp[3]}   | {inp[4]}   | {inp[5]}\n"
          f"---------------\n"
          f"{inp[6]}   | {inp[7]}   | {inp[8]}")


def playerInput(inp: list):
    player_input = int(input("Enter a number between 1 - 9: "))
    if 1 <= player_input <= 9 and inp[player_input - 1] == " ":
        inp[player_input - 1] = player1
    else:
        print("it has been filled")


def check_for_tie(inp: list):
    global running_game
    if " " not in inp:
        print(inp)
        print("it is a tie")
        running_game = False


def check_for_row(inp: list):
    if inp[0] == inp[1] == inp[2] and inp[1] != " ":
        return True
    elif inp[3] == inp[4] == inp[5] and inp[4] != " ":
        return True
    elif inp[6] == inp[7] == inp[8] and inp[6] != " ":
        return True


def check_horizontally(inp: list):
    if inp[0] == inp[3] == inp[6] and inp[0] != " ":
        return True
    elif inp[1] == inp[4] == inp[7] and inp[1] != " ":
        return True
    elif inp[2] == inp[5] == inp[8] and inp[6] != " ":
        return True


def check_diagonal(inp: list):
    if inp[0] == inp[4] == inp[8] and inp[0] != " ":
        return True
    elif inp[2] == inp[4] == inp[6] and inp[4] != " ":
        return True


def check_for_win(inp: list):
    global running_game
    if check_diagonal(inp) or check_horizontally(inp) or check_for_row(inp):
        print("it is a win!")
        running_game = False
    else:
        check_for_tie(board)


def check_for_restart():
    global running_game
    stands = input("Would you like to continue? Y/N ")
    match stands.lower():
        case "y": running_game = True


while running_game:
    print(printBoard(board))
    playerInput(board)
    check_for_win(board)
