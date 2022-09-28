

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


one_yr_one_pc = [[1, 10.0, 1010.0]]
complete_answer = [[1, 4500.00, 104500.00],
                   [2, 4702.50, 109202.50],
                   [3, 4914.11, 114116.61],
                   [4, 5135.25, 119251.86],
                   [5, 5366.33, 124618.19],
                   [6, 5607.82, 130226.01],
                   [7, 5860.17, 136086.18],
                   [8, 6123.88, 142210.06],
                   [9, 6399.45, 148609.51],
                   [10, 6687.43, 155296.94]]


def format_tabular_string(list):
    """Print tabular output as specified in rubric."""
    # header:
    string = f"Year\tInterest\tBalance\n===================================="

    for i in list:
        year = f"{i[0]:2d}"
        interest = f"{i[1]:,.2f}"
        total = i[2]
        # Numeric value justified right
        # Values display appropriate number of decimal places (2)
        # Values have "thousands" seperators
        # All values line up in vertical columns
        string += (f"\n{year:4}\t$ {interest:6}\t$ {total:,.2f}")
    print(string)
    return string


format_tabular_string(complete_answer)

# Header 3
# Value justification (numeric values right justified) 3
# Values display appropriate number of decimal places (2) 3
# Values have “thousands” separators 3
# All values line up in vertical columns

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
