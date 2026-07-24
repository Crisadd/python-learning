def main():
    vanity_plate = input("Vanity Plate: ").upper()
    if is_valid(vanity_plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(vanity_plate):
    numbers = {'0','1','2','3','4','5','6','7','8','9'}
    verification = True
    found_number = False

    if len(vanity_plate) >= 2 and len(vanity_plate) <= 6:

        if vanity_plate[0] not in numbers and vanity_plate[1] not in numbers:

            for i in vanity_plate:
                if not i.isalnum():
                    verification = False
                if i.isdigit():
                    if not found_number:
                        found_number = True
                        if i == "0":
                            verification = False
                elif found_number:
                    verification = False

        else:
            verification = False
    else:
        verification = False

    return verification

if __name__ == "__main__":
    main()