from Helpers.DataTypeHelpers import * 

def test_return_true_if_intable():
    assert isInt("1") == True

def test_return_false_if_not_intable():
    assert isInt("not and int") == False