import time
import concurrent.futures
from p3_persondb import PersonDB
from Lab5_create_people_db import create_people_database

people_db_file = "sqlite.db"
max_people = 500


def load_person(id, db_file):
    """Load DB record in context of PersonDB instance."""
    with PersonDB(db_file) as db:
        return db.load_person(id)


def load_people_tpe_list_comp(worker_threads=10):
    """Use ThreadPoolExecutor to load all people records in DB."""
    print(f"Running with {worker_threads} threads")
    with concurrent.futures.ThreadPoolExecutor(worker_threads) as executor:
        futures = [executor.submit(load_person, x, people_db_file)
                   for x in range(0, max_people)]

    for future in concurrent.futures.as_completed(futures):
        print(future.result())

    return futures

# ================================ Extra Credit ================================


def sort_future_list(future_list):
    """Sort list of futures as tuples."""
    tuple_list = tupleise_futures_list(future_list)
    return sorted(tuple_list, key=lambda x: (x[1], x[2]))


def tupleise_futures_list(future_list):
    """Transform futures into tuples."""
    return [future.result() for future in future_list]


# ================================ Done out of interest ================================

def without_list_comp():
    """Use ThreadPoolExecutor to load all people records in DB WITHOUT list comp."""
    with concurrent.futures.ThreadPoolExecutor(10) as executor:
        futures = []
        for i in range(0, max_people):
            futures.append(executor.submit(load_person, i, people_db_file))

        for future in concurrent.futures.as_completed(futures):
            print(future.result())


def without_tpe():
    """Load all people records in DB without using ThreadPoolExecutor."""
    people = []
    for i in range(0, max_people):
        people.append(load_person(i, people_db_file))

    print(people)

# =======================================================================================

if __name__ == "__main__":
    print("Create people DB")
    create_people_database(people_db_file, max_people) # note - when assessing extra credit, please comment this out 
    # after running it once to confirm that sort_future_list() works correctly (otherwise you get a diff DB each time, &
    # therefore a different alphabetised list).

    with_tpe_start = time.time()
    people_list = load_people_tpe_list_comp()
    with_tpe_finish = time.time() - with_tpe_start

    # Extra credit:
    print(sort_future_list(people_list))

    # ================================ Done out of interest ================================
    # Uncomment below if interested in time differences:

    # without_tpe_start = time.time()
    # without_tpe()
    # without_tpe_finish = time.time() - without_tpe_start

    # with_tpe_without_list_comp_start = time.time()
    # without_list_comp()
    # with_tpe_without_list_comp_finish = time.time() - with_tpe_without_list_comp_start

    # print("With TPE time: ", with_tpe_finish)
    # print("Without TPE time: ", without_tpe_finish)
    # print("With TPE, without list comp time: ", with_tpe_without_list_comp_finish)

# Results:
# With TPE time:  0.09191203117370605
# Without TPE time:  0.10013389587402344
# With TPE, without list comp time:  0.0979909896850586
