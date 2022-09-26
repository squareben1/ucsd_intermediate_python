from p3_compound_interest_calc import * 

# principal; float 0.0 or 0.10 ($)
# apr; float 0.0 or 0.10 (%)
# term; int 1-30 (y)

# Enter the principal amount (ex: 1000.00): 100000 
# Enter interest rate percentage (ex: 4.5): 4.5 
# Enter term in years (ex: 10): 10 
# Year       Interest        Balance 
# ================================== 
#    1  $    4,500.00  $  104,500.00 
#    2  $    4,702.50  $  109,202.50 

def test_get_compound_interest_one_year_1_apr():
    assert get_compound_interest(1000, 1, 1) == [[1, 10.0, 1010.0]]

def test_get_compound_interest_2_year_1_apr():
    assert get_compound_interest(1000, 1, 2) == [[1, 10.0, 1010.0], [2, 20.1, 1020.1]]