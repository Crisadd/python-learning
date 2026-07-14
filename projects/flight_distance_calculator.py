"""
Create a program that calculates the total distance flown.
Requirements
    - Ask the user how many flight legs they completed.
    - For each leg:
            * Ask for the distance in kilometers.
            * Validate that the distance is greater than 0.
    - Display:
        * Total distance
        * Average distance
        * Longest flight
        * Shortest flight
"""


def get_flight_legs():
    flight_legs = int(input("How many flight legs did you fly?: "))

    while flight_legs <= 0:
        print("Invalid number. It must be greater than 0.")
        flight_legs = int(input("How many flight legs did you fly?: "))

    return flight_legs


def collect_flight_data():
    flight_legs = get_flight_legs()
    nautical_miles_legs = []

    for i in range(flight_legs):
        nautical_miles = int(input(f"How many Nautical Miles in leg {i + 1}?: "))

        while nautical_miles <= 0:
            print("Invalid number. It must be greater than 0.")
            nautical_miles = int(input(f"How many Nautical Miles in leg {i + 1}?: "))

        nautical_miles_legs.append(nautical_miles)

    return flight_legs, nautical_miles_legs


def calculate_statistics(flight_legs, nautical_miles_legs):
    total_distance = sum(nautical_miles_legs)
    average_distance = total_distance / flight_legs
    longest_flight = max(nautical_miles_legs)
    shortest_flight = min(nautical_miles_legs)

    return total_distance, average_distance, longest_flight, shortest_flight


def show_results(
    flight_legs,
    nautical_miles_legs,
    total_distance,
    average_distance,
    longest_flight,
    shortest_flight,
):

    print("\nFlight Summary")
    print("+~~~~~~~~~~~~~~~~~~~~~~~~~+")
    print(f"Total Distance: {total_distance} NM")
    print(f"Average Distance: {average_distance:.1f} NM")
    print(f"Longest Flight: {longest_flight} NM")
    print(f"Shortest Flight: {shortest_flight} NM")
    print("+~~~~~~~~~~~~~~~~~~~~~~~~~+")


def main():
    while True:

        flight_legs, nautical_miles_legs = collect_flight_data()

        total_distance, average_distance, longest_flight, shortest_flight = (
            calculate_statistics(flight_legs, nautical_miles_legs)
        )
        show_results(
            flight_legs,
            nautical_miles_legs,
            total_distance,
            average_distance,
            longest_flight,
            shortest_flight,
        )

        question = input("\nWould you like to continue? (y/n): ").lower()

        while question not in ("y", "n"):
            question = input(
                "\nInvalid answer. Would you like to continue? (y/n): "
            ).lower()

        if question == "n":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
