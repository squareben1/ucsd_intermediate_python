import pytest
from src.student import *


class TestStudentClass:
    def test_init_no_courses(self):
        # testing state over behaviour...not ideal
        student = Student(123456, "Johnnie", "Smith")
        assert student.id == 123456
        assert student.firstName == "Johnnie"
        assert student.lastName == "Smith"
        assert type(student.courses) == dict

    def test_init_with_courses(self):
        courses_dict = {
            'CSE-101': 3.50, 'CSE-102': 3.00, 'CSE-201': 4.00, 'CSE-220': 3.75, 'CSE-325': 4.00}
        student = Student(123456, "Johnnie", "Smith", courses_dict)
        assert type(student.courses) == dict
        assert student.courses == courses_dict

    def test_gpa(self):
        courses_dict = {
            'CSE-101': 3.50, 'CSE-102': 3.00, 'CSE-201': 4.00, 'CSE-220': 3.75, 'CSE-325': 4.00}
        student = Student(123456, "Johnnie", "Smith", courses_dict)
        assert student.gpa() == 3.65
