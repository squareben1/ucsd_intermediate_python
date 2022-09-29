
def isInt(string):
    try:
        if isinstance(int(string), int):
            return True
        else:
            return False
    except:
        return False


def isFloat(string):
    try:
        if isinstance(float(string), float):
            return True
        else:
            return False
    except:
        return False
