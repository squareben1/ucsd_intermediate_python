from p2_password_strength_grader import * 

def test_password_length_is_greater_than_or_equal_to_8():
    assert check_password("abcdefgh") == 1