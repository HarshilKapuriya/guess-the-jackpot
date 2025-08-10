import random

jackpot = random.randint(1, 100)

guess = int(input("Guess the jackpot number : "))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower")

    guess = int(input("Guess again: "))
    counter += 1

else:
    print(f"Congratulations! You guessed the jackpot number {jackpot} in {counter} tries.")
    print('Attempts:', counter)