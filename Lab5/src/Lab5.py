import random


def generate_people(count):
    """Generate list of name tuples of count length."""
    last_names = get_names("LastNames.txt")
    first_names = get_names("FirstNames.txt")
    
    tuple_list = []

    rand_num = random.randrange(0, count, 1)

    for i in range(count):
        tuple_list.append((i, first_names[rand_num], last_names[rand_num]))

    return tuple_list

def get_names(filename):
    """Return list of stripped names."""
    names_file = open(f"src/{filename}", "r")
    
    return [i.rstrip() for i in names_file.readlines()]
