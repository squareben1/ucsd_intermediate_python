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

### Part 1: Palindrome Checker

I attempted to use TDD to reach a solution. It might be a stretch to say the final result was completely TDD'ed but the experimentation I went through helped me see that using `length` and a while loop was much simpler. I had overcomplicated things prior to that. At least its properly tested now.

     NOTE: if you want a laugh, feel free to go back through the git history to see how unnecessarily complicated my original not-quite-solution was. I did go down a fun rabbit hole trying to remember how recursion worked then use it in a loop though.

I opted to treat single characters as palindromes for 2 reasons -

1.  its a nice, easy first test (TDD FTW)
2.  the internet said I could: https://english.stackexchange.com/questions/486943/can-a-single-letter-be-a-palindrome#:~:text=Mathematically%2C%20yes%2C%20a%20single%20letter,get%20carried%20away%20just%20yet).

## Part 2: Password Strength Grader

Slightly more successful attempt at TDD. Some slip-ups along the way e.g. when I realised that numbers in strings were being double counted as lower case chars.

Decided not to overcomplicate by turning them into integers with int() function when I'd already created the strip special chars function and could just remove numbers that way.

### NOTE ON BONUS POINTS:

For the password length bonus points I have used the instructions in the PDF itself:

1 point for each:

- Password length is greater than or equal to 8
- password length > 8
- password length >= 16

There appears to be slightly different instructions in the notes section of the webpage for Lab 1:

    1 point for 8-11 chars, 2 points for 12-15 chars and 3 points for 16+ chars.

Although I have gone with the former, the code to meet the second set of criteria would only require a small change and look something like:

    if pw_length >= 8 and pw_length <= 11:
        overall_score += 1

    if pw_length >= 12 and pw_length <= 15:
        overall_score += 1

    if pw_length >= 16:
        overall_score += 1
