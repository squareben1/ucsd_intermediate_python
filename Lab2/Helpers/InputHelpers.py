from Helpers.DataTypeHelpers import *  # Note: Must include folder prefix
import datetime
__all__ = ['inputInt', 'inputFloat', 'inputString', 'inputDate']


def inputInt(prompt="Enter an integer: ", min_value=0, max_value=100):
    """
    Use input() method to display the “prompt” variable and read in a string.
    Loop until input can be parsed into int and is between min and max value.
    """

    while True:
        # loop input prompt
        answer = input(prompt)

        # call isInt
        if isInt(answer) != True:
            # if false print, continue loop
            print("entered text needs to be in the int format...")
            continue
        else:
            # if true convert to int
            integer = int(answer)
            # ensure falls between min_value and max_value inc.
            if integer >= min_value and integer <= max_value:
                return integer
            else:
                print(f"Value must be between {min_value} and {max_value}")
                continue


def inputFloat(prompt="Enter a float: ", min_value=0, max_value=100):
    """
    Use input() method to display the “prompt” variable and read in a string.
    Loop until input can be parsed into float and is between min and max value.
    """

    while True:
        # loop input prompt
        answer = input(prompt)

        # call isFloat
        if isFloat(answer) != True:
            # if false print, continue loop
            print("entered text needs to be in the float format...")
            continue
        else:
            # if true convert to float
            num = float(answer)
            # ensure falls between min_value and max_value inc.
            if num >= min_value and num <= max_value:
                return num
            else:
                print(f"Value must be between {min_value} and {max_value}")
                continue


def inputString(prompt="Enter a string: ", min_length=0, max_length=100):
    """
    Use input() method to display the “prompt” variable and read in a string.
    Loop until length of input is between min and max value.
    """

    while True:
        # loop input prompt
        answer = input(prompt)
        length = len(answer)

        if length >= min_length and length <= max_length:
            return answer
        else:
            print(
                f"Text must be between {min_length} and {max_length} in length")
            continue


def inputDate(prompt="Enter a date in ISO format (yyyy-mm-dd): "):
    """
    Use input() method to display the “prompt” variable and read in a string.
    Loop until input can be parsed into date of yyyy-mm-dd format.
    """

    while True:
        # loop input prompt
        answer = input(prompt)
        if isDate(answer) != True:
            # if false print, continue loop
            print("Value must be a date in “yyyy-mm-dd” format.")
            continue
        else:
            # date = datetime.datetime.strptime(answer, "%Y%m%d").date()
            date = datetime.date.fromisoformat(answer)
            return date
