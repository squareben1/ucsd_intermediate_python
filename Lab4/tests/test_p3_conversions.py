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