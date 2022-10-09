from p3_compound_interest_calc import *


def test_get_compound_interest_one_year_1_apr():
    assert get_compound_interest(1000, 1, 1) == [[1, 10.0, 1010.0]]


def test_get_compound_interest_2_year_1_apr():
    assert get_compound_interest(1000, 1, 2) == [
        [1, 10.0, 1010.0], [2, 10.1, 1020.1]]


def test_provided_numbers():
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
    assert get_compound_interest(100000, 4.5, 10) == complete_answer

# NOTE: I opted not to use TDD for format_tabular_string() as it required a lot of fiddling on my part.
