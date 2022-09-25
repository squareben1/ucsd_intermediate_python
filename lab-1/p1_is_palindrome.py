# Please use for loops in the palindrome method, not a slicer or any other reverse function.

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
    print("Enter a string: ")
    string = input()
    answer = is_palindrome(string)

    output = f"Is '{string}' a palindrome? {answer}"
    print(output)
    return output

if __name__ == "__main__":
    main()

# NOTE: I opted to treat single chaacters as palindromes for 2 reasons - 
# 1. its a nice, easy first test (TDD FTW)
# 2. the internet said I could: https://english.stackexchange.com/questions/486943/can-a-single-letter-be-a-palindrome#:~:text=Mathematically%2C%20yes%2C%20a%20single%20letter,get%20carried%20away%20just%20yet).

# NOTE: if you want a laugh, feel free to go back through the git history to see how 
# unnecessarily complicated my original not-quite-solution was! I did go down a fun rabbit hole
# trying to remember how recursion worked then use it in a loop though. 

# NOTE: did not write test