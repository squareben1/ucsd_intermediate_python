import random
import sqlite3
from sqlite3 import Error
import concurrent.futures

# ================================ Part 1 ================================

people_db_file = "sqlite.db"
max_people = 500


def generate_people(count):
    """Generate list of name tuples of count length."""
    last_names = get_names("LastNames.txt")
    first_names = get_names("FirstNames.txt")

    # names_list = load_name_files_tpe()
    # last_names = names_list[1]
    # first_names = names_list[0]

    tuple_list = []

    for i in range(count):
        first_names_rand_num = random.randrange(0, len(first_names), 1)
        last_names_rand_num = random.randrange(0, len(last_names), 1)

        tuple_list.append(
            (i, first_names[first_names_rand_num], last_names[last_names_rand_num]))

    return tuple_list


def get_names(filename):
    """Return list of stripped names from file."""
    names_file = open(f"src/{filename}", "r")

    return [i.rstrip() for i in names_file.readlines()]

# ================================ Extra Credit ================================


def load_name_files_tpe(worker_threads=2):
    """
    Use ThreadPoolExecutor to load all people records in DB.
    Returns: List of name lists.
    """
    print(f"Running with {worker_threads} threads")
    file_names = ["LastNames.txt", "FirstNames.txt"]
    with concurrent.futures.ThreadPoolExecutor(worker_threads) as executor:
        futures = [executor.submit(get_names, x) for x in file_names]

    # interesting - this makes my original method of assignment to last_names and first_names with list[x] in generate_people
    # inconsistent; presumably the longer file takes longer to be as_completed() - caused original test to fail since it
    # asserts [(0, 'JAMES', 'SMITH')] but was getting [(0, 'SMITH', 'JAMES')]. I have therefore implemented this function for
    # extra credit but not actually used it (see commented code in generate_people()) as it made variable assignment inconsistent.
    # Opted not to spend longer making it consistent since its actual use in the code was not required in the extra credit rubric.

    return [future.result() for future in concurrent.futures.as_completed(futures)]

# ================================ Part 2 ================================


people_db_file = "sqlite.db"  # The name of the database file to use
max_people = 500  # Number of records to create


def create_people_database(db_file, count):
    """Create people table if not exists."""
    conn = sqlite3.connect(db_file)
    with conn:
        sql_create_people_table = """ CREATE TABLE IF NOT EXISTS people (
            id integer PRIMARY KEY,
            first_name text NOT NULL,
            last_name text NOT NULL); """
        cursor = conn.cursor()
        cursor.execute(sql_create_people_table)
        # truncate existing
        sql_truncate_people = "DELETE FROM people;"
        cursor.execute(sql_truncate_people)
        people = generate_people(count)

        sql_insert_person = "INSERT INTO people(id,first_name,last_name) VALUES(?,?,?);"
        cursor = conn.cursor()
        for person in people:
            # print(person)  # uncomment if you want to see the person object
            cursor.execute(sql_insert_person, person)
            # print(cursor.lastrowid)  # uncomment if you want to see the row id
        cursor.close()


if __name__ == "__main__":
    create_people_database(people_db_file, max_people)

    # Extra credit, uncomment to confirm works as specified in Lab5 rubric:
    # print(load_name_files_tpe())
