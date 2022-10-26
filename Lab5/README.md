# Intermediate Python Course - UCSD

## Lab 5

Please note - although the instructions called for my `Lab5_create_people_db.py` to be named simply `Lab5.py`, I opted for a more descriptive name as it made more sense since I was splitting functionality between files - I hope thats OK!

I also left `TestSQLite.py` in the directory for my own records.

### How to Run

`cd` into project directory and run: `export PYTHONPATH="$PWD"`

To run any [program]:

`python3 [program]`

e.g.

`python3 src/Lab5_create_people_db.py`

To run all tests:

`pytest`


### Part 1 & Part 2: Lab5_create_people_db.py

Run the file to create a DB locally:

`python3 src/Lab5_create_people_db.py`

Please note - I didn't use the extra credit load_name_files_tpe() in the program itself since it made assignment of variables inconsistent due to unpredictable order ot first_name and last_name lists in the list it returned. It was almost always [[last_names], [first_names]] but not every time, presumably because FirstNames.txt is a much larger file and therefore takes longer for the future to be as_completed() & added to the list. 


### Part 4: p4_thread_pool_executor.py

I did some experimentation with how long it would take to run with and without the use of ThreadPoolExecutor, as well as with ThreadPoolExecutor but without list comprehension. I have left this code in the file but commented it out so as not to distract from the core functionality specified in the rubric. 

#### Results:

        With TPE time:  0.09191203117370605
        Without TPE time:  0.10013389587402344
        With TPE, without list comp time:  0.0979909896850586


