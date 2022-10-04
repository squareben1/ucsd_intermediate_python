from DataTypeHelpers import isInt


def inputInt(prompt="Enter an integer: ", min_value=0, max_value=100):
    answer = input(prompt)

    while True:
        if isInt(answer) != True:
            print("entered text needs to be in the int format...")
            inputInt()
        else:
            integer = int(answer)
            print(integer)
            return integer


def main():
    """Main Function."""

    inputInt()


if __name__ == "__main__":
    main()
