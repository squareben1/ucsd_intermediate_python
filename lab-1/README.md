# Intermediate Python Course - UCSD

## How to Run

`cd` into project directory and run: `export PYTHONPATH="$PWD"`

To run any [program]:

`python3 [program]`

e.g.

`python3 p1_is_palindrome.py`

To run all tests:

`pytest`

To run tests for specific program:

`pytest [path_to/test_file]`

e.g.

`pytest tests/test_p2_password_strength_grader.py`

## Approach

I attempted to use TDD to reach a solution. 

Reasonable attempt made to keep code DRY and adhere roughly to single responsibility principle. 

### Part 1: Palindrome Checker

It might be a stretch to say the final result was completely TDD'ed but the experimentation I went through helped me land on final, much simpler solution. I had overcomplicated things prior to that. At least its properly tested now.

I opted to treat single characters as palindromes for 2 reasons -

1.  its a nice, easy first test (TDD FTW)
2.  the internet said I could: https://english.stackexchange.com/questions/486943/can-a-single-letter-be-a-palindrome#:~:text=Mathematically%2C%20yes%2C%20a%20single%20letter,get%20carried%20away%20just%20yet).


### Note on Part 2 Bonus Points:

I have scored based on pass word length as per clarified instructions in Discussion board:

    0-7 = 0 points

    8-11 = 1 point

    12-15 = 2 points

    16+ = 3 points
