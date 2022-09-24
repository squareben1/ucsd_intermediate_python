import pytest

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