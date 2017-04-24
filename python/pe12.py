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
    tri_lst = factors2(n)
    while len(tri_lst) <= 100:
        n += 1
        tri_lst = factors(n)
    return reduce(lambda x,y: x*y, tri_lst)


