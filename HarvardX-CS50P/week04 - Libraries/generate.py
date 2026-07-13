import random
# https://docs.python.org/3/library/random.html

# from random import choice
# choice(["heads", "tails"])

coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1,10)
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)

for card in cards: 
    print(card)

