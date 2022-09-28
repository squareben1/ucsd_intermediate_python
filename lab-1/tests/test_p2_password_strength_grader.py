import pytest
import builtins

from p2_password_strength_grader import *


def test_password_length_is_less_than_8():
    assert check_password("abcdef") == 1


def test_password_length_8_to_12():
    assert check_password("abcdefghe") == 2


def test_extra_cred_bonus_more_12_to_15():
    assert check_password("abcdefghijklm") == 3


def test_extra_cred_bonus_more_16():
    assert check_password("abcdefghijklmnopq") == 4


def test_at_least_one_upper_case_letter():
    assert check_password("S") == 1


def test_score_lower_case():
    assert check_password("s") == 1


def test_score_numeric():
    assert check_password("1") == 1


def test_special_char():
    assert check_password("!") == 1


def test_all_adds_up_to_5():
    assert check_password("Abcdef1!") == 5


def test_feature_user_input_pw():
    # mock user input
    builtins.input = lambda: "Abcdef1!"
    assert main() == "Your password score is: 5"
    builtins.input = input


def test_feature_user_input_pw_max_score():
    # mock user input
    builtins.input = lambda: "Abcdefghijklmnopq1!"
    assert main() == "Your password score is: 7"
    builtins.input = input
