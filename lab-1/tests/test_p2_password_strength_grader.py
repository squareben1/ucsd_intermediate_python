from p2_password_strength_grader import * 

def test_password_length_is_greater_than_or_equal_to_8():
    assert check_password("abcdefgh") == 2

def test_at_least_one_upper_case_letter():
    assert check_password("String") == 1

def test_score_zero():
    assert check_password("string") == 1