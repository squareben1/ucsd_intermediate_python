# Intermediate Python Course - UCSD

## Lab 4

The tests constitute part of my answer for Part 3. 

### How to Run

`cd` into project directory and run: `export PYTHONPATH="$PWD"`

To run any [program]:

`python3 [program]`

e.g.

`python3 src/p1_leibniz.py`

To run all tests:

`pytest`


### Part 1: LeibnizPiIterator

Run the file to test:

`python3 src/p1_leibniz.py`

Please note - I didn't do any validation due to time constraint so please input integers only.

Results:

Output:

        pi after 100000 iterations: 3.14158265358979348846264335202950289372841939396495
        Difference: 0.00000999999999975000000003124999999046875000541015

        pi after 10000000 iterations: 3.14159255358979323846289338327950288107216939937520
        Difference: 0.00000009999999999999975000000000000312499999999990

### Part 2: NilakanthaPiGenerator

Run the file to test:

`python3 src/p2_nilakantha.py`

Output:

        pi after 100000 iterations: 3.14159265358979298847014326453044038404101783047277
        Difference: 0.00000000000000024999250011874906250015615156890233

        pi after 1000000 iterations: 3.14159265358979323821264413327831538513466938375109
        Difference: 0.00000000000000000024999925000118749906250001562401

        pi after 10,000,000 iterations: 3.14159265358979323846239338335450287232217033687510
        Difference: 0.00000000000000000000024999992500001187499906250000


### Part 3

The tests for part 3 (in particular those in `test_p3_compose_conversions.py` are intended to to act as my solution. Each requirement in the Lab4 PDF has an associated test demonstrating completion, i.e. each compose function has a test - so the solution is "Convert 2 miles to inches (result: 126720)" is represented in `test_compose_2_miles_inches`: 

        def test_compose_2_miles_inches():
            """Convert 2 miles to inches (result: 126720)"""
            miles_to_inches = compose(miles_to_yards, yards_to_feet, feet_to_inches)
            assert miles_to_inches(2) == 126720

Run `pytest` to run tests. 