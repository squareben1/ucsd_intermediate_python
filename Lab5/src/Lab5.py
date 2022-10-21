import random


def generate_people(count):
    last_names_file = open("src/LastNames.txt", "r")
    last_names = [i.rstrip() for i in last_names_file.readlines()]

    first_names_file = open("src/FirstNames.txt", "r")
    first_names = [i.rstrip() for i in first_names_file.readlines()]
    
    tuple_list = []

    rand_num = random.randrange(0, count, 1)

    for i in range(count):
        tuple_list.append((i, first_names[rand_num], last_names[rand_num]))

    return tuple_list
