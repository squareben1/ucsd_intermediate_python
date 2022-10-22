import random
from sqlite3 import Error

people_db_file = "sqlite.db"  # The name of the database file to use
max_people = 500  # Number of records to create


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
    """Return list of stripped names."""
    names_file = open(f"src/{filename}", "r")

    return [i.rstrip() for i in names_file.readlines()]


if __name__ == "__main__":
    people = generate_people(5)
    print(people)
