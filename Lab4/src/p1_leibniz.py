from fraction import *
from decimal import *


class LeibnizPiIterator:
    def __init__(self):
        pass

    def __iter__(self):
        self.fraction = Fraction(0, 1)  # running total
        self.n = 1  # denominator to be used in the next iteration
        self.add_next = True

        return self

    def __next__(self):
        if self.add_next:
            self.fraction += Fraction(4, self.n)
        else:
            self.fraction -= Fraction(4, self.n)
        self.add_next = not self.add_next
        self.n += 2

        return self.fraction.value


if __name__ == "__main__":
    pi50 = Decimal("3.14159265358979323846264338327950288419716939937510")
    counter = 0
    iterations = int(input("Enter number of iterations: "))

    for x in LeibnizPiIterator():
        counter += 1
        if counter >= iterations:
            break
    print(f"pi after {counter} iterations: {x:.50f}")
    diff = pi50 - x
    print(f"Difference: {diff:0.50f}")


# Output:
# pi after 100000 iterations: 3.14158265358979348846264335202950289372841939396495
# Difference: 0.00000999999999975000000003124999999046875000541015

# pi after 10000000 iterations: 3.14159255358979323846289338327950288107216939937520
# Difference: 0.00000009999999999999975000000000000312499999999990
