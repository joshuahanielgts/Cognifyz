def number_guesser():
    low, high = 1, 50
    number = random.randint(low, high)
    guess = None
    while guess != number:
        guess = int(input(f"Guess a number ({low}-{high}): "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You guessed it!")

# number_guesser()
