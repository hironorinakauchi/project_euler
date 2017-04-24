#first try on my own

from functools import reduce
def triangle_num(n):
    """
    generates a triangular number
    i.g. the 7th triangle number would be 1+2+3+4+5+6+7=28
    triangle_num(7) == 28
    """
    return sum([x for x in range(n+1)])

def factors(n):
    """
    returns a number of factors in a list
    not so efficient for this problem
    """
    lst = []
    for i in range(1,n+1):
        if n % i == 0:
            lst.append(i)
    return lst

def main():
    n = 1
    tri_lst = factors(n)
    while len(tri_lst) <= 100:
        n += 1
        tri_lst = factors(n)
    return reduce(lambda x,y: x*y, tri_lst)

# second try with help of online resources

import math

def get_factors(n):
    """
    returns a number of factors of n.
    note: n % i => False if divisible.
    """
    return sum(2 for i in range(1, round(math.sqrt(n)+1)) if not n % i)

def generate_triangles(limit):
    """
    returns n(n+1)/2 as needed
    """
    l = 1
    while l < limit:
        yield sum(range(1, l+1))
        l += 1

def test_triangles():
    triangles = generate_triangles(100000)
    for i in triangles:
        if get_factors(i) >= 500:
            return i

