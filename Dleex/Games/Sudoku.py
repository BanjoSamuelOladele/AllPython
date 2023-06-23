board = [[], [], [], [], [], [], [], [], []]
num =0
for num in range(board.__len__()):
    inside = 0
    while inside < 9:
        board[num] = board.append(input("Enter "))
        inside += 1

print(board)

for index, n in enumerate(board):
    for ind, m in enumerate(n):
        if m == n[index]:
            print("bye bye")