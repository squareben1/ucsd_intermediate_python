
def check_password(password):
    """Score strenght of password from 0 - 5."""
    score = 0
    upper_case_score = 0
    lower_case_score = 0
    number_score = 0

    if len(password) >= 8:
        score += 1

    for i in password:
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



    return score
