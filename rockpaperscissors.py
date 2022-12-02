import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"
    if isWin(user, computer):
        return "You Win"

    return "You lost"

def isWin(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and
         opponent == "r"):

        return True

print(play())