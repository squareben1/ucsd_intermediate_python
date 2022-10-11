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
        assert student.add_courses(
            {'CSE-102': 3.00}) == {'CSE-101': 3.50, 'CSE-102': 3.00}

    def test___str__(self):
        # 123456    Smith           Johnnie         3.650 CSE-101,CSE-102,CSE-201,CSE-220,CSE-325

        johnnie = Student(123456, "Johnnie", "Smith", {
                          'CSE-101': 3.50, 'CSE-102': 3.00, 'CSE-201': 4.00, 'CSE-220': 3.75, 'CSE-325': 4.00})
        # jamie = Student(234567, "Jamie", "Strauss", {
        #                   'CSE-101': 3.00, 'CSE-103': 3.50, 'CSE-202': 3.25, 'CSE-220': 4.00, 'CSE-401': 4.00})
        # jack = Student(345678, "Jack", "O'Neill", {
        #                   'CSE-101': 2.50, 'CSE-102': 3.50, 'CSE-103': 3.00, 'CSE-104': 4.00})
        # students = [johnnie, jamie, jack]
        # result = students
        assert johnnie.__str__() == '\n123456\t Smith\t Johnnie\t3.65 CSE-101,CSE-102,CSE-201,CSE-220,CSE-325'

# 123456 Johnnie Smith 'CSE-101': 3.50, 'CSE-102': 3.00, 'CSE-201': 4.00, 'CSE-220': 3.75, 'CSE-325': 4.00
# 234567 Jamie Strauss 'CSE-101': 3.00, 'CSE-103': 3.50, 'CSE-202': 3.25, 'CSE-220': 4.00, 'CSE-401': 4.00
# 345678 Jack O'Neill 'CSE-101': 2.50, 'CSE-102': 3.50, 'CSE-103': 3.00, 'CSE-104': 4.00

    def test_get_course_list(self):
        johnnie = Student(123456, "Johnnie", "Smith", {
                          'CSE-101': 3.50, 'CSE-102': 3.00, 'CSE-201': 4.00, 'CSE-220': 3.75, 'CSE-325': 4.00})
        assert johnnie.get_course_list() == "CSE-101,CSE-102,CSE-201,CSE-220,CSE-325"