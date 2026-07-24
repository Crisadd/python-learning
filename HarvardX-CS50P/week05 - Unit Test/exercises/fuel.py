def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(percentage))


def convert(fraction):
    num_x, num_y = fraction.split('/')

    num_x = int(num_x)
    num_y = int(num_y)

    if num_y == 0:
        raise ZeroDivisionError

    if num_x < 0 or num_y < 0 or num_x > num_y:
        raise ValueError

    return round((num_x / num_y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
