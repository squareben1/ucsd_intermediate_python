from Helpers.DataTypeHelpers import *


def test_isInt_return_true_if_intable():
    assert isInt("1") == True


def test_isInt_return_false_if_not_intable():
    assert isInt("not an int") == False


def test_isFloat_return_true_if_floatable():
    assert isFloat("1") == True


def test_isFloat_return_false_if_not_floattable():
    assert isFloat("not a float") == False


# def test_isFloat_return_true_if_floatable():
#     assert isInt("1") == True


# def test_isFloat_return_false_if_not_floattable():
#     assert isInt("not a float") == False
