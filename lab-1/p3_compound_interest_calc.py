# Python II – Lab 1 - Part 3 – Ben Gittins 

# NOTE: I have rounded up to 2 decimal places based on the example given (i.e. when given the
# numbers shown in example (principal = 100000, apr = 4.5, term = 10) my calc showed that interest in
# year 10 was 6687.428131864148, while the example gave it as 6,687.43)

def get_compound_interest(principal, apr, term):
    """
    Calculate interest, principal and total for each year of term.
    Return: list of lists: [[year, interest_amount, new_total]]
    """
    principal = float(principal)
    apr = float(apr)

    calc_list = []

    for i in range(0, term):
        # Correct interest calculation
        interest = principal * (apr / 100.00)
        principal = interest + principal
        calc_list.append([i+1, round(interest, 2), round(principal, 2)])

    return calc_list


def format_tabular_string(list):
    """Print tabular output as specified in rubric."""
    # header:
    string = f"Year\tInterest\tBalance\n===================================="

    for i in list:
        # Proper loop creation (no overflows and all indices visited) 
        year = f"{i[0]:2d}"
        interest = f"{i[1]:,.2f}"
        total = i[2]
        # Numeric value justified right
        # Values display appropriate number of decimal places (2)
        # Values have "thousands" seperators
        # All values line up in vertical columns
        string += (f"\n{year:>4}\t$ {interest:6}\t$ {total:,.2f}")

    print(string)
    return string


def main():
    """
    Get user input, pass to calc. 
    Return results formatted into table.
    """
    # Properly handles user input
    print("Enter the principal amount (ex: 1000.00): ")
    # Proper parsing of input data into variables
    principal = float(input())

    print("Enter interest rate percentage (ex: 4.5): ")
    apr = float(input())

    print("Enter term in years (ex: 10): ")
    term = int(input())

    calc_list = get_compound_interest(principal, apr, term)

    result = format_tabular_string(calc_list)


if __name__ == "__main__":
    main()
