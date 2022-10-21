from fraction import *
from decimal import *


def NilakanthaPiGenerator():
    fraction = Fraction(3, 1)
    num = 2
    add_next = True

    while True:
        x = num
        y = x + 1
        z = y + 1
        operand = Fraction(4, (x * y * z))
        if add_next:
            fraction += operand
        else:
            fraction -= operand
        add_next = not add_next
        num += 2
        yield fraction.value


pi50 = Decimal("3.14159265358979323846264338327950288419716939937510")

iterations = 10000000

if __name__ == "__main__":
    counter = 0
    iterations = int(input("Enter number of iterations: "))
    for x in NilakanthaPiGenerator():
        counter += 1
        if counter >= iterations:
            break
    print(f"pi after {counter} iterations: {x:.50f}")
    diff = pi50 - x
    print(f"Difference: {diff:0.50f}")


# Output:
# pi after 100000 iterations: 3.14159265358979298847014326453044038404101783047277
# Difference: 0.00000000000000024999250011874906250015615156890233

# pi after 1000000 iterations: 3.14159265358979323821264413327831538513466938375109
# Difference: 0.00000000000000000024999925000118749906250001562401

# 10,000,000 seems to take longer than Leibniz... this seems wrong?

# pi after 10,000,000 iterations: 3.14159265358979323846239338335450287232217033687510
# Difference: 0.00000000000000000000024999992500001187499906250000
