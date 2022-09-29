from Helpers.DataTypeHelpers import *


def test_isInt_return_true_if_intable():
    assert isInt("1") == True


def test_isInt_return_false_if_not_intable():
    assert isInt("not an int") == False


def test_isFloat_return_true_if_floatable():
    assert isFloat("1") == True


def test_isFloat_return_false_if_not_floattable():
    assert isFloat("not a float") == False


def test_isDate_return_true_if_dateable():
    assert isDate("19910901") == True


def test_isDate_return_false_if_not_fdateable():
    assert isDate("not a float") == False
