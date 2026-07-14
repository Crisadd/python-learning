"""Ruleta
El jugador apuesta a un número.
La ruleta genera un número aleatorio.
Se calcula si ganó."""

import random

roulette_number = random.randint(0, 36)

print(roulette_number)

bet = int(input("Bet a number (0-36): "))
money_bet = int(input("Money: "))

if bet == roulette_number:
    print(
        f"The number in the roulette was: {roulette_number}. You won USD {money_bet * 35}."
    )
else:
    print(f"You lost {money_bet}")

""" apuestas a rojo/negro,
múltiples apuestas,
saldo del jugador.

Más adelante, si quieres hacer una ruleta más realista, probablemente convenga usar una lista de diccionarios, porque cada apuesta puede tener datos distintos:
bets = [
    {"number": 7, "money": 10},
    {"number": 15, "money": 20}
]

Así puedes tener diferentes montos apostados en cada número.
"""
