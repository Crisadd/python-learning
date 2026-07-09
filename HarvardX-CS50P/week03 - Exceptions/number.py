def main():
    x = get_in()
    print(f'x is {x}')


def get_in():
    while True:
        try:
            x = int(input("What's x? "))

        except ValueError:
            print('x is not an integer')

        else:
            # break
            return x #it breaks the loop and it also return the number


main()