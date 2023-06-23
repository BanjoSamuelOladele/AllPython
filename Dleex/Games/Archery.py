from random import randint
player1 = []
player2 = []
player3 = []
player4 = []
chances, gamer1, gamer2, gamer3, gamer4 = 0, 0, 0, 0, 0
sum1, sum2, sum3, sum4 = 0, 0, 0, 0
archery = {
    'Player 1': player1,
    'Player 2': player2,
    'Player 3': player3,
    'Player 4': player4
}
while chances < 3:
    while gamer1 == chances:
        e = randint(0, 10)
        player1.append(e)
        gamer1 += 1
    while gamer2 == chances:
        e = randint(0, 10)
        player2.append(e)
        gamer2 += 1
    while gamer3 == chances:
        e = randint(0, 10)
        player3.append(e)
        gamer3 += 1
    while gamer4 == chances:
        e = randint(0, 10)
        player4.append(e)
        gamer4 += 1
    chances += 1
print(archery)
for player, score in archery.items():
    scores = sum(score)
    if player == "Player 1":sum1 = scores
    if player == "Player 2":sum2 = scores
    if player == "Player 3": sum3 = scores
    if player == "Player 4": sum4 = scores
    print(f"{player} scores {scores}")
def check():
    if sum1 > sum2 and sum1 > sum3 and sum1 > sum4:
        print("player 1 won")
    if sum2 > sum1 and sum2 > sum3 and sum1 > sum4:
        print("player 2 won")
    if sum3 > sum1 and sum3 > sum2 and sum3 > sum4:
        print("player 3 won")
    if sum4 > sum2 and sum4 > sum3 and sum4 > sum4:
        print("player 4 won")


check()
