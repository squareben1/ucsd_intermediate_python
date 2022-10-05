# Intermediate Python Course - UCSD

## Lab 2

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

### Approach

I attempted to use TDD for the DataTypeHelpers only. 

I favoured simplicity and readability over strict adherence to SRP/DRY principles.

Output matching example given in assigment: 

    ➜  Lab2 git:(main) ✗ python3 HelpersDriver.py
    Please enter a number: -1
    Value must be between 0 and 100
    Please enter a number: 101
    Value must be between 0 and 100
    Please enter a number: 1
    1
    Please enter a number: -10.1
    Value must be between -10 and 1000
    Please enter a number: 1000.1
    Value must be between -10 and 1000
    Please enter a number: 567.123
    567.123
    Enter some text: tiny
    Text must be between 5 and 10 in length
    Enter some text: This is way too long
    Text must be between 5 and 10 in length
    Enter some text: Just right
    Just right
    Enter a date: December 10, 2000
    Value must be a date in “yyyy-mm-dd” format.
    Enter a date: 2000-12-10
    2000-12-10