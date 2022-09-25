
def check_password(password):
    """Score strenght of password from 0 - 5."""
    score = 0
    upper_case = False

    if len(password) >= 8:
        score += 1

    while upper_case == False:
        for i in password:
            if i == i.upper():
                score += 1
                upper_case = True
                break
            if i == i.lower():
                score += 1
                upper_case = True
                break
        break

    return score
