from itertools import*
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
"""

def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q*q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def nth(iterable, n, default = None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)

#=======================================================================================

"""def is_prime(num):
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True
"""

def count():
    curr = 0
    while True:
        yield curr
        curr += 1

def primes_sieve2(limit):
    a = [True] * limit                         # Initialize the primality list
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

