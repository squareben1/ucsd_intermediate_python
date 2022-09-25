# Please use for loops in the palindrome method, not a slicer or any other reverse function.

def is_palindrome(string):
    """Return true if string arg is palindrome, else false."""
    # Homogenise input, remove spaces. 
    fmted_string = string.lower().replace(" ", "")

    # Treat single char as palindrome. 
    if len(fmted_string) < 2:
        return True
    # Remove obvious non-palindromes
    elif fmted_string[0] != fmted_string[-1]:
        return False

    if len(fmted_string) == 3 and fmted_string[0] == fmted_string[-1]:
        return True

    if len(fmted_string) % 2 != 0:
        print("Length of fmted_string = ", len("wasitacaroracatisaw"))
        mid_char = len(fmted_string) // 2
        print("mid_char", mid_char)
        print("fmted_string[:mid_char]", fmted_string[:mid_char])
        print("fmted_string[mid_char:]", fmted_string[mid_char:])
        print("fmted_string[mid_char+1:]", fmted_string[mid_char+1:])

        mid_stripped_str = fmted_string[:mid_char] + fmted_string[mid_char+1:]
        print(mid_stripped_str)
        fmted_string = mid_stripped_str

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
    
    # string_list = [x for x in fmted_string]

    # x = False

    # # Use lenght of list ?
    # first_half
    # second_half 
    # for i in first_half:
    #     if i == second_half
    # for i in string_list:
    #     if i == string_list[-1]:
    #         # print("Match: ", string_list[0], string_list[-1])
    #         # string_list.remove(string_list[0])
    #         # string_list.remove(string_list[-1])
    #         string = "".join(string_list[1:-1])
    #         is_palindrome((string))
    #         x = True
    #     else:
    #         x = False

    # return x

# for odd maybe remove the middle char then do same as four

# note - prof might be looking for grasp of string manipulation (??)
# in which case the list method might be insufficient


is_palindrome("string")

# TODO:
# - input
# - feature test with input & output
# - output:
# Sample Run (User-entered data in RED):
# Enter a string: REDIVIDER
# Is 'REDIVIDER' a palindrome? True


# NOTE: regarding case sensitivity in extra credit criteria;
# Text comparison is case sensitive by default (i.e. Level != level)
# I therefore took it to mean that I should homogenize input
# with .lower()
