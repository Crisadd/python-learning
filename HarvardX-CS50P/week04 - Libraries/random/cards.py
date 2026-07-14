import random

cards = ["jack", "queen", "king"]

def main():
    # print(random.choice(cards)) #choose one
    # print(random.choices(cards, k=2)) # choose two cards because of the parameter K
    # print(random.sample(cards, k=2)) # select without cards repetition.

    # random.seed(0) # Random toma tiene en cuenta los segundos para ver q numero sale. PLantandole una semilla va a ser siempre lo mismo
    print(random.choices(cards, weights=[75, 20, 5], k=2)) #  Weights is the porcentage of elections



main()
