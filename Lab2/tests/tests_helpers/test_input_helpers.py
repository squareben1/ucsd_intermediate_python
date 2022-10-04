import builtins

from Helpers.InputHelpers import *


def test_inputInt_false():
    # mock user input
    builtins.input = lambda: "not an int"
    assert inputInt() == "Enter an integer: "
    builtins.input = input
