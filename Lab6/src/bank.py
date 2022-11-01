from threading import Semaphore, Thread, Lock
from queue import Queue, Empty
from random import randint
from time import sleep
from get_customers import generate_customer_names

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
        return "{self.name}"


class Teller():
    def __init__(self) -> None:
        pass

    def bankprint(lock, msg):
        """Acquire lock, print message, release."""
        with lock:
            print(msg)


if __name__ == "__main__":
    printlock = Lock()
    teller_line = Queue(maxsize=max_customers_in_bank)
    guard = Semaphore(max_customers_in_bank)
    Teller.bankprint(printlock, "<G> Security guard starting their shift")
    Teller.bankprint(printlock, "*B* Bank open")
    
