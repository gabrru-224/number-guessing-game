import random
import math

lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

if lower >= upper:
    print("The upper bound must be greater than the lower bound.")
else:
    secret_number = random.randint(lower, upper)
    chances = math.ceil(math.log2(upper - lower + 1))
    count = 0
    won = False

    print("You have", chances, "chances to guess!")

    while count < chances:
        guess = int(input("Guess a number: "))
        count += 1

        if guess == secret_number:
            print("Congratulations! You won in", count, "tries!")
            won = True
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    if not won:
        print("The secret number was", secret_number)
        print("Better luck next time!")
