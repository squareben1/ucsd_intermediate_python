
def isInt(string):
    try:
        return True if isinstance(int(string), int) else False
    except:
        return False


def isFloat(string):
    try:
        return True if isinstance(float(string), float) else False
    except:
        return False
