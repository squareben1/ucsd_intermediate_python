

def get_compound_interest(principal, apr, term):
    """
    Calculate interest, principal and total for each year of term.
    Return: list of lists: [[year, interest_amount, new_total]]
    """
    principal = float(principal)
    apr = float(apr)

    calc_list = []

    for i in range(0, term):
        interest = principal * (apr / 100.00)
        new_principal = interest + principal
        calc_list.append([i+1, interest, new_principal])

    print(calc_list)
    return calc_list

# def print_compound_int_output():
    # print(f"{apr:>12,.2f} ")
    # define a string with:
    # Year       Interest        Balance
    # ==================================
    # then append to it
    # seperate
