

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
        principal = interest + principal
        calc_list.append([i+1, round(interest, 2), round(principal, 2)])

    print(calc_list)
    return calc_list


def format_tabular_string(list):
    # print(f"{apr:>12,.2f} ")
    string = """Year       Interest        Balance 
    =================================="""

    return f"{apr:>12,.2f} "
    # define a string with:
    # Year       Interest        Balance
    # ==================================
    # then append to it
    # seperate

# >>> d = {1: ["Python", 33.2, 'UP'],
# ... 2: ["Java", 23.54, 'DOWN'],
# ... 3: ["Ruby", 17.22, 'UP'],
# ... 10: ["Lua", 10.55, 'DOWN'],
# ... 5: ["Groovy", 9.22, 'DOWN'],
# ... 6: ["C", 1.55, 'UP']
# ... }
# >>> print ("{:<8} {:<15} {:<10} {:<10}".format('Pos','Lang','Percent','Change'))
# Pos      Lang            Percent    Change    
# >>> for k, v in d.items():
# ...     lang, perc, change = v
# ...     print ("{:<8} {:<15} {:<10} {:<10}".format(k, lang, perc, change))

# NOTE: I have chosen to round up to 2 decimal places based on the example given (i.e. when given the
# numbers shown in example (principal = 100000, apr = 4.5, term = 10) my calc showed that interest in
# year 10 was 6687.428131864148, while the example gave it as 6,687.43)
