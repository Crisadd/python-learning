""" Coke Machine

Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 
25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time
informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change 
the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""

amount_due = 50

print(f'Amount Due: {amount_due}')
while True:
    insert_coin = int(input('Insert Coin: '))
    
    if insert_coin in (25, 10, 5):
    # if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        amount_due -= insert_coin

        if amount_due > 0:
            print(f'Amount Due: {amount_due}')
        else:
            print(f'Change Owed: {abs(amount_due)}')
            break
    else: 
        print(f'Amount Due: {amount_due}')

