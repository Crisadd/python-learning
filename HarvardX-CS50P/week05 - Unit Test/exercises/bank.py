def main():
    greeting = input('Greeting --> ')
    pay = value(greeting)

    print(f'${pay}')


def value(greeting):
    greeting.strip().lower()
    if 'hello' in greeting:
        pay = 0
    elif greeting[0]== 'h':
        pay = 20
    else:
        pay = 100

    return pay


if __name__ == "__main__":
    main()
