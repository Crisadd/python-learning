""" It is correct but i want to order by sorted

with open('names.txt', "r") as file: # R means READ
    for line in file:
        print('Hello,', line.rstrip())

"""

# SORTED
names = []

with open('names.txt', "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f'Hello, {name}')

