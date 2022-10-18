from src.p3_conversions import * 

def test_miles_yards():
    assert miles_to_yards(1) == 1760

def test_miles_yards_2():
    assert miles_to_yards(2) == 3520

def test_yards_miles():
    assert yards_to_miles(1) == 0.0005681818181818

def test_yards_feet():
    assert yards_to_feet(1) == 3

def test_feet_yards():
    assert feet_to_yards(1) == 0.3333333333333333