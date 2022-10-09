import pytest 
from src.student import *

class TestStudentClass:
    def test_init_no_courses(self):
        student = Student(123456, "Johnnie", "Smith")
        assert student.id == 123456
        assert student.firstName == "Johnnie"
        assert student.lastName == "Smith"


# 'CSE-101': 3.50, 'CSE-102': 3.00, 'CSE-201': 4.00, 'CSE-220': 3.75, 'CSE-325': 4.00