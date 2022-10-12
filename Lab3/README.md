# Intermediate Python Course - UCSD

## Lab 3

### How to Run

`cd` into project directory and run: `export PYTHONPATH="$PWD"`

To run any [program]:

`python3 [program]`

e.g.

`python3 HelpersDriver.py`

To run all tests:

`pytest`

To run tests for specific program:

`pytest [path_to/test_file]`

e.g.

`pytest tests/tests_helpers/test_data_type_helpers.py`

### Part 1

Student class defined in `src/student.py`, corresponding tests should demonstrate adherence to rubric, can be run with `pytest` from root. 

### Part 2 

List of students populated in line with instructions outlined in rubric, this is done when the file is called: `python3 src/print_students.py` 

#### PRINTED OUTPUT OF `src/print_students.py`: 


    ID       Last Name      First Name      GPA  Courses
    ==========================================================================================
    123456   Smith          Johnnie         3.650 CSE-101,CSE-102,CSE-201,CSE-220,CSE-325
    234567   Strauss        Jamie           3.550 CSE-101,CSE-103,CSE-202,CSE-220,CSE-401
    345678   O'Neill        Jack            3.250 CSE-101,CSE-102,CSE-103,CSE-104
    456789   Marks          Susie           3.400 CSE-101,CSE-103,CSE-301,CSE-302,CSE-310
    567890   Marks          Frank           3.300 CSE-102,CSE-104,CSE-201,CSE-202,CSE-203
    654321   Marks          Annie           3.900 CSE-101,CSE-102,CSE-103,CSE-201,CSE-203
    456987   Smith          John            3.250 CSE-101,CSE-103,CSE-210,CSE-260
    987456   Smith          Judy            3.700 CSE-102,CSE-103,CSE-201,CSE-210,CSE-310
    111354   Williams       Kelly           3.400 CSE-101,CSE-102,CSE-201,CSE-202,CSE-203
    995511   Williams       Brad            3.400 CSE-102,CSE-110,CSE-125,CSE-201,CSE-203


### Part 3

Queries and new student list created in `src/part_3_queries.py` by simply passing courses to `__init__`'s courses parameter. 

Run file to see output: `python3 src/part_3_queries.py`

