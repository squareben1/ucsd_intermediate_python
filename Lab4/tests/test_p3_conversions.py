from src.p3_conversions import * 

def test_miles_yards():
    assert miles_to_yards(1) == 1760

def test_miles_yards_2():
    assert miles_to_yards(2) == 3520