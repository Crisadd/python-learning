"""
I've selected a secret number between 1 and 100. Guess what it is, and I'll tell you if your number is too high, too low,
or spot on! What is your first guess?
"""

import random


def guessing():
    target_number = random.randint(1, 100)
    attempts = 1

    while True:
        try:
            guess = int(input("What is your guess?: "))
            if not 1 <= guess <= 100:
                print("Choose a number between 1 and 100.")
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
