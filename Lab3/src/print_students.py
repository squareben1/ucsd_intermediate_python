from student import Student

johnnie = Student(123456, "Johnnie", "Smith")
jamie = Student(234567, "Jamie", "Strauss")
jack = Student(345678, "Jack", "O'Neill")
susie = Student(456789, "Susie", "Marks")
frank = Student(567890, "Frank", "Marks")
annie = Student(654321, "Annie", "Marks")
john = Student(456987, "John", "Smith", {'CSE-101': 2.50, 'CSE-103': 3.00, 'CSE-210': 3.50, 'CSE-260': 4.00})
judy = Student(987456, "Judy", "Smith", {'CSE-102': 4.00, 'CSE-103': 4.00, 'CSE-201': 3.00, 'CSE-210': 3.50, 'CSE-310': 4.00})
kelly = Student(111354, "Kelly", "Williams", {'CSE-101': 3.50, 'CSE-102': 3.50, 'CSE-201': 3.00, 'CSE-202': 3.50, 'CSE-203': 3.50})
brad = Student(995511, "Brad", "Williams", {'CSE-102': 3.00, 'CSE-110': 3.50, 'CSE-125': 3.50, 'CSE-201': 4.00, 'CSE-203': 3.00})
# The remaining 4 student objects are to be created where the courses are passed to __init__’s courses parameter 
# which is a dictionary containing all the courses and scores.

students = [johnnie, jamie, jack, susie, frank, annie, john, judy, kelly, brad]

course_dicts_list = [
{'CSE-101': 3.50, 'CSE-102': 3.00, 'CSE-201': 4.00, 'CSE-220': 3.75, 'CSE-325': 4.00},
{'CSE-101': 3.00, 'CSE-103': 3.50, 'CSE-202': 3.25, 'CSE-220': 4.00, 'CSE-401': 4.00},
{'CSE-101': 2.50, 'CSE-102': 3.50, 'CSE-103': 3.00, 'CSE-104': 4.00},
{'CSE-101': 4.00, 'CSE-103': 2.50, 'CSE-301': 3.50, 'CSE-302': 3.00, 'CSE-310': 4.00},
{'CSE-102': 4.00, 'CSE-104': 3.50, 'CSE-201': 2.50, 'CSE-202': 3.50, 'CSE-203': 3.00},
{'CSE-101': 4.00, 'CSE-102': 4.00, 'CSE-103': 3.50, 'CSE-201': 4.00, 'CSE-203': 4.00},
{'CSE-101': 2.50, 'CSE-103': 3.00, 'CSE-210': 3.50, 'CSE-260': 4.00}
# {'CSE-102': 4.00, 'CSE-103': 4.00, 'CSE-201': 3.00, 'CSE-210': 3.50, 'CSE-310': 4.00},
# {'CSE-101': 3.50, 'CSE-102': 3.50, 'CSE-201': 3.00, 'CSE-202': 3.50, 'CSE-203': 3.50},
# {'CSE-102': 3.00, 'CSE-110': 3.50, 'CSE-125': 3.50, 'CSE-201': 4.00, 'CSE-203': 3.00}
]

def print_students(student_list):
    """Print student list with a header."""
    print(Student.header())
    
    for student in student_list:
        print(student.__str__())


if __name__ == "__main__":
    # At least 3 students must be created without passing an argument to __init__’s courses parameter.
    # - The courses then must be added using individual calls to the student object’s addCourse() method
    for (student, course_dict) in zip(students[:3], course_dicts_list[:3]):
        for key, value in course_dict.items():
            student.add_course(key, value)

    # At least 3 students must be created without passing an argument to __init__’s courses parameter
    # - The courses then must be added using a call to the student object’s addCourses() method using a dictionary.
    for (student, course_dict) in zip(students[3:6], course_dicts_list[3:6]):
        student.add_courses(course_dict)


    print_students(students)
