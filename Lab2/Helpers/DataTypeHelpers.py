__all__ = ['isInt', 'isFloat', 'isDate']


import datetime


def isInt(string):
    """Return True is string is parsable into integer, else False."""
    return check_type(string, int)


def isFloat(string):
    """Return True is string is parsable into float else False."""
    return check_type(string, float)


def check_type(string, check_type):
    """Return True is string is parsable into given type (check_type), else False."""
    # does this sacrifice some readabiity for sake of DRY? Worth it?
    try:
        return True if isinstance(check_type(string), check_type) else False
    except:
        return False


def isDate(string):
    """Return True is string is parsable into date type, else False."""
    try:
        # date = datetime.datetime.strptime(string, "%Y%m%d").date()
        date = datetime.date.fromisoformat(string)
        return True if isinstance(date, datetime.date) else False
    except:
        return False
