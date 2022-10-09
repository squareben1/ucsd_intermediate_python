import pytest
from src.student import *


class TestStudentClass:
    def create_student(self):
        courses_dict = {
            'CSE-101': 3.50, 'CSE-102': 3.00, 'CSE-201': 4.00, 'CSE-220': 3.75, 'CSE-325': 4.00}
        student = Student(123456, "Johnnie", "Smith", courses_dict)
        return student, courses_dict

    def test_init_no_courses(self):
        # testing state over behaviour...not ideal
        student = Student(123456, "Johnnie", "Smith")
        assert student.id == 123456
        assert student.firstName == "Johnnie"
        assert student.lastName == "Smith"
        assert type(student.courses) == dict

    def test_init_with_courses(self):
        student = self.create_student()[0]
        courses_dict = self.create_student()[1]
        assert type(student.courses) == dict
        assert student.courses == courses_dict

    def test_gpa(self):
        student = self.create_student()[0]
        courses_dict = self.create_student()[1]
        assert student.gpa() == 3.65

    def test_gpa_none(self):
        student = Student(123456, "Johnnie", "Smith")
        print(student.courses)
        assert student.gpa() == 0

    def test_add_course(self):
        courses_dict = {'CSE-101': 3.50}
        student = Student(123456, "Johnnie", "Smith", courses_dict)
        assert student.add_course(
            'CSE-102', 3.00) == {'CSE-101': 3.50, 'CSE-102': 3.00}

    def test_add_course_not_float(self):
        courses_dict = {'CSE-101': 3.50}
        student = Student(123456, "Johnnie", "Smith", courses_dict)
        assert student.add_course(
            'CSE-102', "not a float") == {'CSE-101': 3.50}

    def test_add_courses(self):
        courses_dict = {'CSE-101': 3.50}
        student = Student(123456, "Johnnie", "Smith", courses_dict)
        assert student.add_courses({'CSE-102': 3.00}) == {'CSE-101': 3.50, 'CSE-102': 3.00}
