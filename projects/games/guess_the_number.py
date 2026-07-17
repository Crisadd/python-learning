"""
I've selected a secret number between 1 and 100. Guess what it is, and I'll tell you if your number is too high, too low,
or spot on! What is your first guess?
"""

import random


def guessing():
    n_max = int(input("Max number: "))
    target_number = random.randint(1, n_max)
    attempts = 1

    while True:
        try:
            guess = int(input("What is your guess?: "))
            if not 1 <= guess <= n_max:
                print(f"Choose a number between 1 and {n_max}.")
                continue

            attempts += 1

            if guess < target_number:
                print("The number is greater.")

            elif guess > target_number:
                print("The number is lower.")

            else:
                print(
                    f"You guessed the number in {attempts} attempts. Congratulations!"
                )
                break

        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        guessing()

        answer = input("Want to try again? y/n: ").lower()
        if answer == "y":
            guessing()
        else:
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()


"""Guessing Game
I’m thinking of a number between 1 and 100…

What is it?
It’s 50! But what if it were more random?

In a file called game.py, implement a program that:

    - Prompts the user for a level, 𝑛. If the user does not input a positive integer, the program should prompt again.
    - Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
    - Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
        * If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
        * If the guess is larger than that integer, the program should output Too large! and prompt the user again.
        * If the guess is the same as that integer, the program should output Just right! and exit.

HINTS:
    - Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html. Of particular interest, perhaps, are the functions specialized for returning integers, such as randint and randrange.
"""
"""
import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        else:
            secret = random.randint(1, level)
            #print(secret)   ONLY FOR TEST      ONLY FOR TEST       ONLY FOR TEST       ONLY FOR TEST       ONLY FOR TEST
    except ValueError:
        continue

    while True:
        try:
            guess = int(input("Guess the number: "))
            if guess < 1:
                continue
            else:
                if guess < secret:
                    print("Too small!")
                elif guess > secret:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
        except ValueError:
            continue

    break
    """
