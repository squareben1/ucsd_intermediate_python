# Python II – Lab 1 - Part 1 – Ben Gittins 

def is_palindrome(string):
    """Return true if string arg is palindrome, else false."""
    # Homogenise input, remove spaces.
    fmted_string = string.lower().replace(" ", "")

    # Treat single char as palindrome.
    if len(fmted_string) < 2:
        return True

    length = len(fmted_string)
    first = 0
    last = length - 1

    x = False

    while first < last:
        if fmted_string[first] == fmted_string[last]:
            x = True
            first += 1
            last -= 1
        else:
            x = False
            break
    return x


def main():
    """Get user input, check if palindrome. Return formatted string with answer."""
    print("Enter a string: ")
    string = input()
    answer = is_palindrome(string)

    output = f"Is '{string}' a palindrome? {answer}"
    print(output)
    return output


if __name__ == "__main__":
    main()


# def f(string):
#     if len(string) < 2:
#         return True
#     return f(string[1:-1]) if string[0] == string[-1] else False


# def is_palindrome(string):
#     fmted_string = string.lower().replace(" ", "")
#     return f(fmted_string)
