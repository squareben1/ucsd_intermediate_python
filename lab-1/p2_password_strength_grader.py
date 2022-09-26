
def check_password(password):
    """Score strenght of password from 0 - 5."""
    score = 0
    upper_case_score = 0
    lower_case_score = 0
    number_score = 0
    special_char_score = 0

    if len(password) >= 8:
        print("Add 1 for + 8")
        score += 1

    for i in password:
        if i in "!@#$%^&*":
            print("Add 1 for special char")
            special_char_score += 1
        if i in "123456789":
            print("Add 1 for special char")
            number_score += 1

    # strip special chars to avoid double count.
    stripped_pw = strip_special_characters_numbers(password)

    for i in stripped_pw:
        if i == i.upper():
            print("Add 1 for upper")
            upper_case_score += 1
        if i == i.lower():
            print("Add 1 for lower")
            lower_case_score += 1

    if upper_case_score > 0:
        score += 1

    if lower_case_score > 0:
        score += 1

    if number_score > 0:
        score += 1

    if special_char_score > 0:
        score += 1

    return score


def strip_special_characters_numbers(password):
    """Remove special characters & numbers from string."""
    special_chars = "!@#$%^&*123456789"
    special_chars_stripped_pw = ''.join(
        c for c in password if c not in special_chars)
    return special_chars_stripped_pw
