
def is_palindrome(string):
    if len(string) == 1:
        return True
    elif string[0] != string[-1]:
        return False
        
