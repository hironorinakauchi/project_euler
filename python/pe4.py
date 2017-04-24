from itertools import product
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_pelindrome(n):
    return str(n) == str(n)[::-1]

def pelindrome_maker():
    return max(n*m for n in range(1, 1000) for m in range(1, 1000) if is_pelindrome(n*m))

def mul():
    max_pal = 0
    for i in range(100, 999):
        for y in range(100, 999):
            if is_pelindrome(i * y):
                if i * y > max_pal:
                    max_pal = i * y
    return max_pal
