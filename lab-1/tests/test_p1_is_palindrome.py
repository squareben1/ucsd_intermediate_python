import pytest

from p1_is_palindrome import *

def test_one_char_is_palindrome():
    assert is_palindrome('a') == True

def test_non_pal_false():
    assert is_palindrome('not') == False

def test_mom_true():
    assert is_palindrome("mom") == True