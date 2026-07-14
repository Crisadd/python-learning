"""q apis se pueden usar en python para practicar
https://pokeapi.co/
https://rickandmortyapi.com/
https://open-meteo.com/
"""

import sys
import requests

pokemon = input("Pokemon: ").lower()

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

content = response.json()
print(content)

for stats in content["stats"]:
    # print(f'* {stats["base_stat"]}')
    print(f'{stats["stat"]["name"]}: {stats["base_stat"]}')
