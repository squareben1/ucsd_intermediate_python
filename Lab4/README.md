Notes:

**You MUST use the above Fraction module and NOT the fractions module that comes with Python.**  The Python-module does not use decimals and therefore will not yield accurate answers past 12 decimal places.  Plus, it appears to be slower.

- Your results may not match my document 1-for-1.  This could be due to when the value is printed (at iterations or iterations - 1).  As long as your are close (within 1%) then it is fine.
- Please do not pass the number of iterations to perform into the generator or iterator.  They should run indefinitely until the CALLER decides to quit.  Here is an example of a driver for LeinizPiIterator:

        counter = 0
        for x in LeibnizPiIterator():
            counter += 1
            if counter >= iterations: break
        print(f"pi after {counter} iterations: {x:.50f}")
        diff = pi50 - x
        print(f"Difference: {diff:0.50f}")

- Please use the compose lambda/reduce trick I showed in the demos for the compositions.  The other way is just nasty.

        compose = lambda *F: reduce(lambda f, g: lambda x: f(g(x)), F)

TODO: Refresh lambdas 