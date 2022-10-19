from src.p3_conversions import *

# NOTE: Please accept these tests as evidence of successful completion of Part 3.


def test_compose_miles_to_feet():
    # Example given in
    miles_to_feet = compose(miles_to_yards, yards_to_feet)
    assert miles_to_feet(1) == 5280

def test_compose_2_miles_inches():
    miles_to_inches = compose(miles_to_yards, yards_to_feet, feet_to_inches)
    assert miles_to_inches(2) == 126720
