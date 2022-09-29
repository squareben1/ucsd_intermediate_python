__all__ = ['isInt', 'isFloat', 'isDate']
# ^ correct?

import datetime


def isInt(string):
    return check_type(string, int)


def isFloat(string):
    return check_type(string, float)


def check_type(string, check_type):
    try:
        return True if isinstance(check_type(string), check_type) else False
    except:
        return False


def isDate(string):
    try:
        date = datetime.datetime.strptime(string, "%Y%m%d").date()
        return True if isinstance(date, datetime.date) else False
    except:
        return False
