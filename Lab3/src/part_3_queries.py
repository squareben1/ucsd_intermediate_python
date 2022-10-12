
import itertools
from student import Student
from print_students import print_students

johnnie = Student(123456, "Johnnie", "Smith", {'CSE-101': 3.50, 'CSE-102': 3.00, 'CSE-201': 4.00, 'CSE-220': 3.75, 'CSE-325': 4.00})
jamie = Student(234567, "Jamie", "Strauss", {'CSE-101': 3.00, 'CSE-103': 3.50, 'CSE-202': 3.25, 'CSE-220': 4.00, 'CSE-401': 4.00})
jack = Student(345678, "Jack", "O'Neill", {'CSE-101': 2.50, 'CSE-102': 3.50, 'CSE-103': 3.00, 'CSE-104': 4.00})
susie = Student(456789, "Susie", "Marks", {'CSE-101': 4.00, 'CSE-103': 2.50, 'CSE-301': 3.50, 'CSE-302': 3.00, 'CSE-310': 4.00})
frank = Student(567890, "Frank", "Marks", {'CSE-102': 4.00, 'CSE-104': 3.50, 'CSE-201': 2.50, 'CSE-202': 3.50, 'CSE-203': 3.00})
annie = Student(654321, "Annie", "Marks", {'CSE-101': 4.00, 'CSE-102': 4.00, 'CSE-103': 3.50, 'CSE-201': 4.00, 'CSE-203': 4.00})
john = Student(456987, "John", "Smith", {'CSE-101': 2.50, 'CSE-103': 3.00, 'CSE-210': 3.50, 'CSE-260': 4.00})
judy = Student(987456, "Judy", "Smith", {'CSE-102': 4.00, 'CSE-103': 4.00, 'CSE-201': 3.00, 'CSE-210': 3.50, 'CSE-310': 4.00})
kelly = Student(111354, "Kelly", "Williams", {'CSE-101': 3.50, 'CSE-102': 3.50, 'CSE-201': 3.00, 'CSE-202': 3.50, 'CSE-203': 3.50})
brad = Student(995511, "Brad", "Williams", {'CSE-102': 3.00, 'CSE-110': 3.50, 'CSE-125': 3.50, 'CSE-201': 4.00, 'CSE-203': 3.00})


students = [johnnie, jamie, jack, susie, frank, annie, john, judy, kelly, brad]

# QUERIES 

def q1_sort_alphabetically_asc(student_list):
    """Sort the list by lastName, firstName, both in ascending order, and print the results using printStudents()."""
    sorted_list = sorted(student_list, key=lambda student: (student.firstName, student.lastName))
    
    print("List of students sorted by Name: ")
    print_students(sorted_list)
    
    return sorted_list


def q2_sort_gpa_desc(student_list):
    """Sort the list by GPA in descending order and print the results using printStudents()."""
    sorted_list = sorted(student_list, key=lambda student: student.gpa(), reverse=True)
    
    print("List of students sorted by GPA: ")
    print_students(sorted_list)

    return sorted_list


def q3_get_unique_courses(student_list):
    unique_courses = set()

    for student in student_list:
        # bonus: set comprehension
        {unique_courses.add(key) for key in student.courses.keys()}

    print(f"These are the {len(unique_courses)} unique_courses: ", unique_courses)


def q4_list_students_taken_course(student_list, course="CSE-201"):
    """List students who have taken `CSE-201` and print the list using printStudents()."""
    students_have_taken_course = [student for student in student_list if course in student.courses.keys()]

    print(f"These are the {len(students_have_taken_course)} students who have taken {course}: ")
    print_students(students_have_taken_course)


def q5_list_honor_roll_students(student_list):
    """List students who have taken `CSE-201` and print the list using printStudents()."""
    honor_roll = [student for student in student_list if student.gpa() >= 3.5]

    print(f"These are the {len(honor_roll)} students with GPAs >= 3.5: ")
    print_students(honor_roll)

if __name__ == "__main__":
    q1_sort_alphabetically_asc(students)
    print("#"*100)

    q2_sort_gpa_desc(students)
    print("#"*100)

    q3_get_unique_courses(students)
    print("#"*100)

    q4_list_students_taken_course(students)
    print("#"*100)
    
    q5_list_honor_roll_students(students)
    