from Helpers.DataTypeHelpers import *


def test_isInt_return_true_if_intable():
    assert isInt("1") == True

# catch leading negative -
def test_isInt_return_true_if_negative_intable():
    assert isInt("-1") == True

# catch leading positive +
def test_isInt_return_true_if_positive_intable():
    assert isInt("+1") == True


def test_isInt_return_false_if_not_intable():
    assert isInt("not an int") == False


def test_isInt_float_return_false_not_intable():
    assert isInt("1.0") == False

# 1 is a float, so that is legal.
# 1.0 is not an int, so false.

def test_isFloat_return_true_if_floatable():
    assert isFloat("1") == True


def test_isFloat_return_false_if_not_floattable():
    assert isFloat("not a float") == False


def test_isDate_return_true_if_dateable():
    assert isDate("1991-09-01") == True

def test_isDate_return_true_if_no_dashes_dateable():
    assert isDate("19910901") == False


def test_isDate_return_false_if_not_dateable():
    assert isDate("not a date") == False
