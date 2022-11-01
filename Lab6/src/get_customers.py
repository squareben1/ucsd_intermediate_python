import random

def generate_customer_names(count):
    """Generate list of name tuples of count length."""
    last_names = get_names("LastNames.txt")
    first_names = get_names("FirstNames.txt")

    name_list = []

    for i in range(count):
        first_names_rand_num = random.randrange(0, len(first_names), 1)
        last_names_rand_num = random.randrange(0, len(last_names), 1)

        name_list.append(first_names[first_names_rand_num] + " " + last_names[last_names_rand_num])

    return name_list


def get_names(filename):
    """Return list of stripped names from file."""
    names_file = open(f"src/{filename}", "r")

    return [i.rstrip() for i in names_file.readlines()]