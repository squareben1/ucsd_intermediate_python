from threading import Semaphore, Thread, Lock
from queue import Queue, Empty
from random import randint
from time import sleep


# maximum number of customers that can be in the bank at one time
max_customers_in_bank = 10
max_customers = 30  # number of customers that will go to the bank today
max_tellers = 3  # number of tellers working today
teller_timeout = 10  # longest time that a teller will wait for new customers


class Customer():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Teller():
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self):
        return self.name

# • *B* for bank messages
# • <G> for security guard messages
# • [T] for teller messages
# • (C) for customer messages


def bankprint(lock, msg):
    """Acquire lock, print message, release."""
    with lock:
        print(msg)


def wait_outside_bank(customer, guard, teller_line, printlock):
    """Add customer to teller_line queue."""
    bankprint(printlock, f"(C) '{customer}' waiting outside bank")
    guard.acquire()

    try:
        bankprint(
            printlock, f"<G> Secuirty Guard letting '{customer}' into the bank.")
        bankprint(printlock, f"(C) '{customer}' getting into line")
        teller_line.put(customer)
    except:
        print("Error in wait_outside_bank")


def teller_job(teller, guard, teller_line, printlock):
    """Teller help customer."""
    bankprint(printlock, f"[T] {teller} starting work")
    while True:
        try:
            customer = teller_line.get(timeout=teller_timeout)
            bankprint(printlock, f"[T] {teller} is now helping '{customer}'")
            sleep(randint(1, 4))
            bankprint(
                printlock, f"[T] {teller} is done helping '{customer}'.")
            bankprint(
                printlock, f"<G> Security Guard is letting '{customer}' out of the bank.")
            guard.release()
        except Empty:
            bankprint(
                printlock, f"[T] Nobody is in line, '{teller}' going on break.")
            break


if __name__ == "__main__":
    printlock = Lock()
    teller_line = Queue(maxsize=max_customers_in_bank)
    guard = Semaphore(max_customers_in_bank)

    bankprint(printlock, msg=f"<G> Security guard starting their shift")
    bankprint(printlock, "*B* Bank open")

    customers = [Customer(f"Customer {i}") for i in range(max_customers)]

    waiting_customers = [Thread(target=wait_outside_bank, args=(
        customer, guard, teller_line, printlock)).start() for customer in customers]

    sleep(5)

    bankprint(printlock, "*B* Tellers beginning work")

    tellers = [Teller(f"Teller {i}") for i in range(max_tellers)]

    teller_jobs = [Thread(target=teller_job, args=(
        teller, guard, teller_line, printlock)) for teller in tellers]

    for job in teller_jobs:
        job.start()

    for job in teller_jobs:
        job.join()

    bankprint(printlock, "*B* Bank closed.")
    exit
