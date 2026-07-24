# https://docs.python.org/3/library/functions.html#open

name = input("What's your name? ")

# file = open("names.txt", "a")     W means WRITE, A means APPEND
# file.write(f'{name}\n')
# file.close

# Una forma para no tener q olvidarse de cerrar el archivo con file.close
with open("names.txt", "a") as file:
    file.write(f'{name}\n')

