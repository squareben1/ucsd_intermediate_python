import random
import sqlite3
from sqlite3 import Error

# part_1


def generate_people(count):
    """Generate list of name tuples of count length."""
    last_names = get_names("LastNames.txt")
    first_names = get_names("FirstNames.txt")

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

# part 2


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
    # people = generate_people(5)
    # print(people)
    create_people_database(people_db_file, max_people)
