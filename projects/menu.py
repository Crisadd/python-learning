import flight_distance_calculator, airport_database, games.guess_the_number

menu = {
    1: "Flight Distance Calculator",
    2: "Small Airport Database",
    3: "Game: Guess The Number",
    4: "Roulette",
    0: "Exit",
}

while True:
    try:
        print("========= MENU =========")
        for key, value in menu.items():
            print(f"{key} - {value}")

        answer = int(input("Select a number: "))

        match answer:
            case 1:
                flight_distance_calculator.main()
            case 2:
                airport_database.main()
            case 3:
                games.guess_the_number.main()
            case 4:
                games.roulette.main()

            case 0:
                print("Goodbye!")
                break
            case _:
                print("Invalid option.")

    except ValueError:
        print("Invalid number.")
