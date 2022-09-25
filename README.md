# Intermediate Python Course - UCSD 

## Part 1: Palindrome Checker 

To run program: 
    
`python3 p1_is_palindrome.py`

To run tests:

`pytest`

### Approach 

I attempted to use TDD to reach a solution. It might be a stretch to say the final result was completely TDD'ed but the experimentation I went through helped me see that using `length` and a while loop was much simpler. I had overcomplicated things prior to that. At least its properly tested now. 

     NOTE: if you want a laugh, feel free to go back through the git history to see how unnecessarily complicated my original not-quite-solution was! I did go down a fun rabbit hole trying to remember how recursion worked then use it in a loop though.

I opted to treat single characters as palindromes for 2 reasons -
 
 1. its a nice, easy first test (TDD FTW)
 2. the internet said I could: https://english.stackexchange.com/questions/486943/can-a-single-letter-be-a-palindrome#:~:text=Mathematically%2C%20yes%2C%20a%20single%20letter,get%20carried%20away%20just%20yet).

## Part 2: Password Strength Grader