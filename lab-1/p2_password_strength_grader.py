
def check_password(password):
    """Score strength of password from 0 - 5."""
    overall_score = check_length(password)
    upper_case_score = 0
    lower_case_score = 0
    number_score = check_string_contains(password, "123456789")
    special_char_score = check_string_contains(password, "!@#$%^&*")

    # strip special chars & numbers to avoid double count.
    stripped_pw = strip_special_characters_numbers(password)

    for i in stripped_pw:
        # check for upper and lower case chars
        if i == i.upper():
            upper_case_score += 1
        if i == i.lower():
            lower_case_score += 1

    overall_score += tally_final_score(upper_case_score,
                                       lower_case_score, number_score, special_char_score)

    return overall_score


def check_length(password):
    """Calculate length-based score."""
    pw_length = len(password)
    length_score = 0

    # 0-7 = 0 points
    if pw_length >= 8:
        # 8-11 = 1 point
        length_score += 1

    if pw_length >= 12:
        # 12-15 = 2 points
        length_score += 1

    if pw_length >= 16:
        # 16+ = 3 points
        length_score += 1
    return length_score


def check_string_contains(password, string):
    contains_score = 0
    for i in password:
        if i in string:
            contains_score += 1

    return contains_score


def strip_special_characters_numbers(password):
    """Remove special characters & numbers from string."""
    special_chars = "!@#$%^&*123456789"
    special_chars_stripped_pw = ''.join(
        c for c in password if c not in special_chars)

    return special_chars_stripped_pw


def tally_final_score(upper_case_score,
                      lower_case_score, number_score, special_char_score):
    final_score = 0
    if upper_case_score > 0:
        final_score += 1

    if lower_case_score > 0:
        final_score += 1

    if number_score > 0:
        final_score += 1

    if special_char_score > 0:
        final_score += 1
    
    return final_score


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
