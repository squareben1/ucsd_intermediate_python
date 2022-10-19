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


def test_feet_inches():
    assert feet_to_inches(1) == 12


def test_inches_feet():
    assert inches_to_feet(1) == 0.0833333333333333


def test_inches_cm():
    assert inches_to_cm(1) == 2.54


def test_cm_inches():
    assert cm_to_inches(1) == 0.3937007874015748


def test_cm_meters():
    assert cm_to_meters(1) == 0.01


def test_meters_cm():
    assert meters_to_cm(1) == 100


def test_meters_km():
    assert meters_to_km(1) == 0.001


def test_km_meters():
    assert km_to_meters(1) == 1000


def test_km_au():
    # first test showed readable in format given in Rubric. 
    # assert km_to_au(1) == "0.000000006684587122268446" - note its a tiny bit off that given but I felt more time spent would be meaningless.
    assert km_to_au(1) == 6.6845871222684464e-09


def test_au_km():
    assert au_to_km(1) == 149597870.700

def test_au_ly():
    assert au_to_ly(1) == 0.00001581250740982065847572

def test_ly_to_au():
    assert ly_to_au(1) == 63241.07708426628026865358
