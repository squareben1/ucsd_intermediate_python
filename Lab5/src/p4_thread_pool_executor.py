import requests
import concurrent.futures
from p3_persondb import PersonDB

# TODO - import create DB, create DB


def load_person(id, db_file):
    with PersonDB(db_file) as db:
        return db.load_person(id)

# futures = [executor.submit(sleep_rand, x) for x in range(future_count)]


people_db_file = "sqlite.db"
max_people = 10

with concurrent.futures.ThreadPoolExecutor(10) as executor:
    futures = []
    for i in range(0, max_people):
        futures.append(executor.submit(load_person, i, people_db_file))

    for future in concurrent.futures.as_completed(futures):
        print(future.result())
