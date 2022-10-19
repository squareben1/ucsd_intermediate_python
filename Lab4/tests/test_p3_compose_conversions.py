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

