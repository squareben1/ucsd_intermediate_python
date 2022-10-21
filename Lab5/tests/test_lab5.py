from src.Lab5 import *
import unittest.mock as mock


def mock_randrange(value, value2, value3):
    return 0


def test_generate_people_1():
    with mock.patch('random.randrange', mock_randrange):
        assert generate_people(1) == [(0, 'JAMES', 'SMITH')]
