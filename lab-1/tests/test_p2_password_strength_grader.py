import pytest
import builtins

from p2_password_strength_grader import *


def test_password_length_is_greater_than_or_equal_to_8():
    assert check_password("abcdefgh") == 2


def test_at_least_one_upper_case_letter():
    assert check_password("S") == 1


def test_score_lower_case():
    assert check_password("s") == 1


def test_score_numeric():
    assert check_password("1") == 1


def test_special_char():
    assert check_password("!") == 1


def test_all_adds_up_to_5():
    assert check_password("Abcdefgh1!") == 5


def test_feature_user_input_pw():
    # mock user input
    builtins.input = lambda: "Abcdefgh1!"
    assert main() == "Your password score is: 5"
    builtins.input = input
