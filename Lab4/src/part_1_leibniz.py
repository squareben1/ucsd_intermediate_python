from fraction import *
# from Fraction import *
from decimal import *

pi50 = Decimal("3.14159265358979323846264338327950288419716939937510")

iterations = 100000 #0


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
        print("self.fraction.value", self.fraction.value)
        return self.fraction.value


counter = 0
for x in LeibnizPiIterator():
    # print(x)
    counter += 1
    if counter >= iterations:
        break
print(f"pi after {counter} iterations: {x:.50f}")
diff = pi50 - x
print(f"Difference: {diff:0.50f}")
