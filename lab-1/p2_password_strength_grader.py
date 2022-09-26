
def check_password(password):
    """Score strenght of password from 0 - 5."""
    overall_score = 0
    upper_case_score = 0
    lower_case_score = 0
    number_score = 0
    special_char_score = 0
    pw_length = len(password)

    if pw_length >= 8:
        # point if more than or equal to 8
        overall_score += 1
    
    if pw_length > 8:
        # bonus point if more than 8 and less than 16
        overall_score += 1

    if pw_length >= 16:
        # bonus point if more than 16
        overall_score += 1

    for i in password:
        if i in "!@#$%^&*":
            special_char_score += 1
        if i in "123456789":
            number_score += 1

    # strip special chars & numbers to avoid double count.
    stripped_pw = strip_special_characters_numbers(password)

    for i in stripped_pw:
        if i == i.upper():
            upper_case_score += 1
        if i == i.lower():
            lower_case_score += 1

    if upper_case_score > 0:
        overall_score += 1

    if lower_case_score > 0:
        overall_score += 1

    if number_score > 0:
        overall_score += 1

    if special_char_score > 0:
        overall_score += 1

    return overall_score


def strip_special_characters_numbers(password):
    """Remove special characters & numbers from string."""
    special_chars = "!@#$%^&*123456789"
    special_chars_stripped_pw = ''.join(
        c for c in password if c not in special_chars)

    return special_chars_stripped_pw


def main():
    """Get user input, rate password with score. Return formatted string with score."""
    print("Enter a password: ")
    password = input()
    answer = check_password(password)

    output = f"Your password score is: {answer}"
    print(output)
    return output


if __name__ == "__main__":
    main()
