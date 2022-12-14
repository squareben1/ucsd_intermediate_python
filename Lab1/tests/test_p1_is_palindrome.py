import pytest
import builtins

from p1_is_palindrome import *


def test_one_char_is_palindrome():
    assert is_palindrome('a') == True


def test_non_pal_false():
    assert is_palindrome('not') == False


def test_three_letter_true():
    assert is_palindrome("mom") == True


def test_four_letter_true():
    assert is_palindrome("deed") == True


def test_four_letter_false():
    assert is_palindrome("dead") == False


def test_five_letter_true():
    assert is_palindrome("level") == True


def test_nine_chars():
    assert is_palindrome("REDIVIDER") == True


def test_extra_cred_case_sensitivity():
    assert is_palindrome("Level") == True


def test_extra_cred_sentences():
    assert is_palindrome("Was it a car or a cat I saw") == True


def test_feature_user_input():
    # mock user input
    builtins.input = lambda: "REDIVIDER"
    assert main() == "Is 'REDIVIDER' a palindrome? True"
    builtins.input = input
