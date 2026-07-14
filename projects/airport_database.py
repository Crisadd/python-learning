"""Build a small airport database.

Requirements:
- Store at least 10 ICAO airport codes.
- Ask the user to enter an ICAO code.
- Print the airport name.
- If the code doesn't exist, print:
    * Airport not found.
"""

airport_database = {
    "SABE": "Buenos Aires - Aeroparque Jorge Newbery",
    "SAEZ": "Buenos Aires - Ministro Pistarini (Ezeiza)",
    "SADF": "San Fernando",
    "SADM": "Morón",
    "SADP": "El Palomar",
    "SACO": "Córdoba - Ingeniero Taravella",
    "SAME": "Mendoza - El Plumerillo",
    "SAAR": "Rosario - Islas Malvinas",
    "SAAV": "Santa Fe - Sauce Viejo",
    "SAAP": "Paraná - General Justo José de Urquiza",
    "SAZS": "San Carlos de Bariloche",
    "SAZN": "Neuquén - Presidente Perón",
    "SAWG": "Río Gallegos - Piloto Civil Norberto Fernández",
    "SAWH": "Ushuaia - Malvinas Argentinas",
    "SAWE": "Río Grande",
    "SASA": "Salta - Martín Miguel de Güemes",
    "SANT": "Tucumán - Teniente Benjamín Matienzo",
    "SARE": "Resistencia",
    "SARC": "Corrientes",
    "SARF": "Formosa",
    "SARI": "Puerto Iguazú - Cataratas del Iguazú",
    "SAVC": "Comodoro Rivadavia",
    "SAVT": "Trelew",
    "SAVY": "El Tehuelche - Puerto Madryn",
    "SAZY": "San Martín de los Andes - Chapelco",
    "SAZM": "Mar del Plata - Astor Piazzolla",
    "SAZB": "Bahía Blanca - Comandante Espora",
    "SAOC": "Río Cuarto",
    "SAOU": "San Luis",
    "SAOR": "Villa Reynolds",
    "SAAC": "Concordia",
    "SAZR": "Santa Rosa",
    "SAZA": "Azul",
    "SAVR": "Alto Río Senguer",
    "SAWR": "Gobernador Gregores",
}


def get_code():
    icao_code = input("Enter an ICAO code: ").upper()
    return icao_code


def searching_code(code):
    if code in airport_database:
        print(f"Code {code} is {airport_database[code]}")
    else:
        print("Airport not found.")


def show_dictionary():
    for key, value in airport_database.items():
        print(f"{key} - {value}")


def add_new_airport():
    new_airport_icao = input("ICAO airport to add: ").upper()
    new_airport_name = input("Name of the new airport: ")
    airport_database.update({new_airport_icao: new_airport_name})
    print(
        f'The new airport "{new_airport_icao} - {new_airport_name}" has been added successfully\n'
    )


def delete_airport():
    delete_airport_icao = input("ICAO airport to delete: ").upper()
    airport = airport_database.pop(delete_airport_icao, None)

    if airport == None:
        print("Airport not found.")
    else:
        print(f"Airport {delete_airport_icao} has been deleted successfully\n")


def main():
    quantity_of_searches = 0
    while True:
        print("========= MENU =========")
        print("1 - Search airport by ICAO")
        print("2 - Show all airports")
        print("3 - Add a new airport")
        print("4 - Delete an airport")
        print("5 - Total airports")

        print("0 - Exit")
        option = int(input("Option: "))

        if option == 1:
            while True:
                icao_code = get_code()
                searching_code(icao_code)
                quantity_of_searches += 1

                answer = input("Would you like to continue searching? y/n: ")

                while answer not in ("y", "n"):
                    answer = input(
                        "Would you like to continue searching? y/n: "
                    ).lower()

                if answer != "y":
                    print(
                        f">>>>>>>>>>>> You have done {quantity_of_searches} search/es. <<<<<<<<<<<<\n\t\tGoodbye"
                    )
                    break
        elif option == 2:
            show_dictionary()
        elif option == 3:
            add_new_airport()
        elif option == 4:
            delete_airport()
        elif option == 5:
            print(f"Total airports: {len(airport_database)}")
        elif option == 0:
            print("Thank you for using this program.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()


""" Pythonic way
airport = airport_database.get(get_code)
if airport:
    print(airport)
else:
    print("Airport not found.")
"""
