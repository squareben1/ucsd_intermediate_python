from Helpers.DataTypeHelpers import isInt


def inputInt(prompt="Enter an integer: ", min_value=0, max_value=100):
    """
    Use input() method to display the “prompt” variable and read in a string.
    Loop until input can be intified and is between min and max value.
    """

    while True:
        answer = input(prompt)
        if isInt(answer) != True:
            print("entered text needs to be in the int format...")
            continue
        else:
            integer = int(answer)
            if integer >= min_value and integer <= max_value:
                print(integer)
                return integer
            else:
                print("value is out of range ")
                continue


def main():
    """Main Function."""

    inputInt()


if __name__ == "__main__":
    main()
