"""q apis se pueden usar en python para practicar
https://pokeapi.co/
https://rickandmortyapi.com/
https://open-meteo.com/
"""

import sys
import requests
import random

pokemon = input("Pokemon: ").lower()


response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")


content = response.json()
print(content)

for stats in content["stats"]:
    # print(f'*{stats["stat"]["name"]}: {stats["base_stat"]},')

    if stats["stat"]["name"] == "attack":
        poke1_attack = int(stats["base_stat"])

print(f"{poke1_attack}")

for i in range(1, poke1_attack):
    daño = random.randint(1, poke1_attack)
    print(f"El daño de {pokemon} is {daño}")

# def battle_pokemon (pokemon1, pokemon2):
