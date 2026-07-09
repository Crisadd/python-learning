""" Fuel Gauge

Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full,
1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein X is a non-negative
integer and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains,
output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

HINTS:
    - Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including split.
    - Note that you can handle two exceptions separately with code like:
            try:
                ...
            except ValueError:
                ...
            except ZeroDivisionError:
                ...

        Or you can handle two exceptions together with code like:
            try:
                ...
            except (ValueError, ZeroDivisionError):
                ...
"""

def request_fraction():
    return input('Fraction: ').strip()

def get_percentage():

   while True:
        try:
            num_x, num_y = request_fraction().split('/')
            num_x, num_y = int(num_x), int(num_y)

            if num_x > num_y:
                continue
    
            if  num_x < 0:
                continue

            calculation = round((num_x / num_y)*100)
            
            return calculation

        except ValueError:
            #print('It is not and intenger.')
            pass
        except ZeroDivisionError:
            #print('Division by zero is not allowed.')
            pass


def main():
    calculation = get_percentage()

    if calculation <= 1:
        print('E')
    elif calculation >= 99:
        print('F')
    else:
        print(f'{calculation}%')

main()
