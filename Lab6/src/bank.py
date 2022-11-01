from threading import Semaphore, Thread, Lock
from queue import Queue, Empty
from random import randint
from time import sleep
from customer_generation.get_customers import generate_customer_names

# maximum number of customers that can be in the bank at one time
max_customers_in_bank = 10
max_customers = 30  # number of customers that will go to the bank today
max_tellers = 3  # number of tellers working today
teller_timeout = 10  # longest time that a teller will wait for new customers

# • *B* for bank messages
# • <G> for security guard messages
# • [T] for teller messages
# • (C) for customer messages


class Customer():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        # put (C) in string?
        return "{self.name}"


class Teller():
    def __init__(self) -> None:
        pass

    def bankprint(lock, msg):
        """Acquire lock, print message, release."""
        with lock:
            print(msg)


def wait_outside_bank(customer, guard, teller_line, printlock):
    # print customer is waiting outside the bank
    print(f"(C) {customer} is waiting outside bank")
    # try acquire semaphore from guard (NOT in with cntxt mgr)
    guard.acquire()

    try:
        # print security gurard msg saying customer left bank
        print(f"<G> Customer {customer} has entered bank.")
        # print customer msg saying trying to get in line
        print(f"(C) {customer} is trying to get in line")
        # put customer in teller_line queue using queue's put()
        print(f"(C) {customer} is joining teller_line")
        teller_line.put(customer)
    finally:
        print("Release")
        # release at some point


if __name__ == "__main__":
    printlock = Lock()
    teller_line = Queue(maxsize=max_customers_in_bank)
    guard = Semaphore(max_customers_in_bank)
    Teller.bankprint(printlock, "<G> Security guard starting their shift")
    Teller.bankprint(printlock, "*B* Bank open")

    customers = generate_customer_names(max_customers)

    jobs = [Thread(target=wait_outside_bank, args=(
        customers[i], guard, teller_line, printlock)).start() for i in range(max_customers)]
    
    sleep(5)
    # for job in jobs:
    #     print("job before start: ", job)
    #     job.start()
    #     print("Job after start: ", job)
