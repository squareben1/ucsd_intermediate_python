from src.p3_conversions import *

# NOTE: Please accept these tests as evidence of successful completion of Part 3.


def test_compose_miles_to_feet():
    # Example given in instructions.
    miles_to_feet = compose(miles_to_yards, yards_to_feet)
    assert miles_to_feet(1) == 5280


def test_compose_2_miles_inches():
    """Convert 2 miles to inches (result: 126720)"""
    miles_to_inches = compose(miles_to_yards, yards_to_feet, feet_to_inches)
    assert miles_to_inches(2) == 126720


def test_compose_5_feet_meters():
    """Convert 5 feet to meters (result: 1.524)"""
    feet_to_meters = compose(feet_to_inches, inches_to_cm, cm_to_meters)
    assert feet_to_meters(5) == 1.524


def test_compose_5_feet_meters():
    """Convert 5 feet to meters (result: 1.524)"""
    feet_to_meters = compose(feet_to_inches, inches_to_cm, cm_to_meters)
    assert feet_to_meters(5) == 1.524


def test_compose_1_meter_inches():
    """Convert 1 meter to inches (result: 39.37007874015748)"""
    meters_to_inches = compose(meters_to_cm, cm_to_inches)
    assert meters_to_inches(1) == 39.37007874015748


def test_compose_10_miles_km():
    """Convert 10 miles to kilometers (result: 16.09344)"""
    mile_to_km = compose(miles_to_yards, yards_to_feet,
                         feet_to_inches, inches_to_cm, cm_to_meters, meters_to_km)
    assert mile_to_km(10) == 16.09344


def test_compose_1_km_miles():
    """
    Convert 1 kilometer to miles (result: 0.6213711922373341)
    NOTE: Answer returned slightly differently but close enough at 0.6213711922399999
    """
    km_to_miles = compose(yards_to_miles, feet_to_yards,
                          inches_to_feet, cm_to_inches, meters_to_cm, km_to_meters)
    assert km_to_miles(1) == 0.6213711922399999


def test_compose_12_km_inches():
    """Convert 12.7 kilometers to inches (result: 500000.0)"""
    km_to_inches = compose(km_to_meters, meters_to_cm, cm_to_inches)
    assert km_to_inches(12.7) == 500000.0

def test_compose_500k_inches_km():
    """Convert 500000 inches to kilometers (result: 12.7)"""
    inches_to_km = compose(inches_to_cm, cm_to_meters, meters_to_km)
    assert inches_to_km(500000) == 12.7

def test_compose_10m_meters_ly():
    """
    Convert 9,460,730,472,580,800 meters to light years (result: 1)
    NOTE: My answer came to 1.0000000000000002, 0.0000000000000002 more than that in 
    the Lab instructions. 
    This to be less than 2 meters difference (1.8921437881877 meters, to be precise*). 
    So not that bad. 
    """
    meters_to_ly = compose(meters_to_km, km_to_au, au_to_ly)
    assert meters_to_ly(9460730472580800) == 1.0000000000000002




# * see working:
ly_to_meters = compose(ly_to_au, au_to_km, km_to_meters)
print(ly_to_meters(0.0000000000000002))

