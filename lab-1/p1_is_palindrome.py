
def is_palindrome(string):
    if len(string) == 1:
        return True
    elif string[0] != string[-1]:
        return False

    if len(string) == 3 and string[0] == string[-1]:
        return True



is_palindrome("string")
