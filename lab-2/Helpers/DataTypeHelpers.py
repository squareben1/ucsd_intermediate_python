import datetime


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


def isDate(string):
    try:
        date = datetime.datetime.strptime(string, "%Y%m%d").date()
        return True if isinstance(date, datetime.date) else False
    except:
        return False

# datetime.datetime.strptime("19910901", "%d%m%Y").date()
