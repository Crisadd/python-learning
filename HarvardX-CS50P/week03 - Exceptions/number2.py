# Same exrcise, fewer lines

def main():
    x = get_in()
    print(f'x is {x}')


def get_in():
    error = 0
    while True:
        try:
            return int(input("What's x? "))

        except ValueError:
            # print('x is not an integer')
            error +=1
            if error > 3:
                print(f'It is not and intenger')
            else:
                pass


main()