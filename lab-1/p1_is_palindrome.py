
def is_palindrome(string):
    if len(string) == 1:
        return True
    elif string[0] != string[-1]:
        return False

    if len(string) == 3 and string[0] == string[-1]:
        return True

    # length = len(string)

    string_list = [x for x in string]

    # print(string_list[length-1])
    # print(string_list)

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
