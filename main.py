import random

def guess(x):
    randomNum = random.randint(1, x)
    guess = 0

    while guess != randomNum:
        guess = int(input(f"guess a number between 1 and {x}"))
        if guess < randomNum:
            print("sorry, guess again. Too Low.")
        elif guess > randomNum:
            print("sorry, guess again. Too High.")

    print(f"You got it dicknuts! It was {randomNum}")

def compGuess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            gues = low
        feedback = input(f"is {guess} too high (H), too low (L), or correct (C)")
        if feedback == "h":
            high = guess - 1
        if feedback == "l":
            low = guess + 1

    print(f"I got it, it's {guess}!")

compGuess(2000)