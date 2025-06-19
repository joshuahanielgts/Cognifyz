import random

def guessing_game():
    number = random.randint(1, 100)
    guess = None
    while guess != number:
        guess = int(input("Guess a number (1-100): "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct!")

# guessing_game()
