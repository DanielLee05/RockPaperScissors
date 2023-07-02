import random


def player_turn():
    while True:
        move = input("Choose rock, paper, or scissors. Rock represents 1, paper is 2, and scissors is 3: ")
        if move.isdigit():
            move = int(move)
            if 0 < move < 4:
                break
            else:
                print("Must choose a valid number.")
        else:
            print("Must choose a valid number.")
    return move


def ai_turn():
    value = random.randint(1, 3)
    return value


def main():
    your_move = player_turn()
    ai_move = ai_turn()

    if ai_move == your_move:
        print("Tied.")
    elif ai_move == 1:
        if your_move + ai_move == 3:
            print("You Win")
        else:
            print("You Lose")
    elif ai_move == 2:
        if your_move + ai_move == 3:
            print("You Lose")
        else:
            print("You Win")
    elif ai_move == 3:
        if your_move + ai_move == 4:
            print("You Win")
        else:
            print("You Lose")

main()