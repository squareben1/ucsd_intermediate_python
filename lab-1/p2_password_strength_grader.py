
def check_password(password):
    """Score strenght of password from 0 - 5."""
    score = 0
    upper_case_score = 0
    lower_case_score = 0
    number_score = 0
    special_char_score = 0

    if len(password) >= 8:
        score += 1

    for i in password:
        if i in "!@#$%^&*":
            special_char_score += 1

    special_chars_stripped_pw = strip_special_characters(password)

    for i in special_chars_stripped_pw:
        if i == i.upper():
            upper_case_score += 1
        if i == i.lower():
            lower_case_score += 1
        if isinstance(i, int):
            number_score += 1

    if upper_case_score > 0:
        score += 1

    if lower_case_score > 0:
        score += 1

    if number_score > 0:
        score += 1

    if special_char_score > 0:
        score += 1

    return score


def strip_special_characters(password):
    """Remove special characters from string"""
    special_chars = "!@#$%^&*"
    special_chars_stripped_pw = ''.join(
        c for c in password if c not in special_chars)
    return special_chars_stripped_pw
