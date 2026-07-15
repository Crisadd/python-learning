"""Little Professor
One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems 
for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to 
display 4 + 1 = , David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. 
And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:
    - Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
    - Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits. No need to support operations other than addition (+).
    
    * Note: The order in which you generate x and y matters. Your program should generate random numbers in x, y pairs to simulate generating one math question at a time (e.g., x0 with y0, x1 with y1, and so on).
    
    - Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
    - The program should ultimately output the user’s score: the number of correct answers out of 10.

Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a single randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
import random

def main():
    ...

def get_level():
    ...

def generate_integer(level):
    ...

if __name__ == "__main__":
    main()

HINTS:
    - Note that you can raise an exception like ValueError with code like:
        raise ValueError
    - Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html. Of particular interest, perhaps, are the functions specialized for returning integers, such as randint and randrange.
"""
import random

def get_level():
    while True:
        try:
            level = int(input('Level: '))

            if 1 <= level <= 3:
                return level

        except ValueError:
            pass

def run_quiz(prompt):
    score = 0

    match prompt:
        case 1:
            for i in range (10):
                number_x= random.randint(0,9)
                number_y= random.randint(0,9)
                attemps = 0

                while attemps < 3:
                    try:
                        addition = int(input(f'{number_x} + {number_y} = '))

                        if addition != (number_x + number_y):
                            attemps +=1
                            print('EEE')

                        else:
                            score +=1
                            break
                    except ValueError:
                        attemps +=1
                        print('EEE')
                else:
                    print(f'{number_x} + {number_y} = {number_x + number_y}')

        case 2:
            for i in range (10):
                number_x= random.randint(10,99)
                number_y= random.randint(10,99)
                attemps = 0

                while attemps < 3:
                    try:
                        addition = int(input(f'{number_x} + {number_y} = '))

                        if addition != (number_x + number_y):
                            attemps +=1
                            print('EEE')

                        else:
                            score +=1
                            break
                    except ValueError:
                        attemps +=1
                        print('EEE')
                else:
                    print(f'{number_x} + {number_y} = {number_x + number_y}')
        case 3:
            for i in range (10):
                number_x= random.randint(100,999)
                number_y= random.randint(100,999)
                attemps = 0

                while attemps < 3:
                    try:
                        addition = int(input(f'{number_x} + {number_y} = '))

                        if addition != (number_x + number_y):
                            attemps +=1
                            print('EEE')

                        else:
                            score +=1
                            break
                    except ValueError:
                        attemps +=1
                        print('EEE')
                else:
                    print(f'{number_x} + {number_y} = {number_x + number_y}')

    return score

def main():
    level = get_level()
    score = run_quiz(level)
    print(f'Score: {score}')

if __name__ == "__main__":
    main()
