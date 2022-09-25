
def check_password(password):
    """Score strenght of password from 0 - 5."""
    score = 0
    upper_case_score = 0
    lower_case_score = 0

    if len(password) >= 8:
        score += 1

    for i in password:
        if i == i.upper():
            upper_case_score += 1
        if i == i.lower():
            lower_case_score += 1

    if upper_case_score > 0:
        score += 1

    if lower_case_score > 0:
        score += 1
        # break

    # while lower_case == False:
    #     for i in password:
    #         if i == i.lower():
    #             score += 1
    #             lower_case = True
    #             break
    #     break

    return score
