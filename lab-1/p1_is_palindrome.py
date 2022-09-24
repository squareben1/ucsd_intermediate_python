# Please use for loops in the palindrome method, not a slicer or any other reverse function.

def is_palindrome(string):
    """Return true if string arg is palindrome, else false."""
    string = string.lower()
    
    if len(string) == 1:
        return True
    elif string[0] != string[-1]:
        return False

    if len(string) == 3 and string[0] == string[-1]:
        return True

    string_list = [x for x in string]

    x = False

    for i in string_list:
        if string_list[0] == string_list[-1]:
            string_list.remove(i)
            string_list.remove(string_list[-1])
            x = True
        else:
            x = False

    return x

# for odd maybe remove the middle char then do same as four


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