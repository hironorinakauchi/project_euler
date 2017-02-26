"""
Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence 
whose values do not exceed four million, 
find the sum of the even-valued terms.
"""

def even_fib():
	total = 0
	n1, n2 = 1,1
	while n1 < 4000000:
		if n1 % 2 == 0:
			total += n1
		n1, n2 = n2, n1 + n2
	print(total)

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

from math import sqrt
def F(n):
    x = ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
    return int(x)


"""
None of these functions but the first does work.
Another way to think about this problem is that if you compute
the first few numbers...
1 1 2 3 5 8 13 21 34 55 89 144...
a b c a b c  a  b c  a  b  c

"""

"""
the function below does not work because it literally computes
the values 4000000 times, so what this returns is 4000000th fibonacci
number which is not what we want. 
what we do want is the sum of THE VALUES THAT DO NOT EXCEED 4000000.
the issues here is that you set up a counter seprately from the value n1.
if you want a sequence whose value does not exceed 4000000,
you need to keep track of the value, not the anumber of times to compute.

"""


def even_fib2():
	total = 0
	k = 1
	n1, n2 = 1,2
	while k < 4000000:
		if n1 % 2 == 0:
			total += n1
		n1, n2 = n2, n1 + n2
		k += 1
	print(total)

# fibinacci sequence

def fib(n):
	"""the n Fibonacci number, N>=0"""
	assert n >= 0
	if n <= 1:
		return n
	else:
		return fib(n-2) + fib(n-1)

# but this function takes long time to compute so...

def fib2(fk1, fk, k, n):
	"""assuming Fk1 and Fk2 are fib(k-1) and fib(k) in the Fibonacci
	sequence and that N>=K, return fib(N)."""
	if n == k: return fk
	else:	   return fib2(fk, fk1+fk, k+1, n)
def fib(n):
	if n <= 1: return n
	else:	   return fib2(0, 1, 1, n)

# or you can turn one of these above into iteration like below
# optimization: since the var. n doesn't change, just leave it off

def fib3(n):
	if n <= 1: return n
	fk1, fk, k = 0, 1, 1
	while n != k:
		fk1, fk, k = fk, fk1+fk, k+1
	return fk

# but fib2 is just an auxiliary function. you can tuck it away inside fib
# called "nested function"

def fib(n):
	def fib2(fk1, fk, k):
		if n == k: return fk
		else:	   return fib2(fk, fk1 + fk, k+1)
	if n <= 1:	return n
	else: 		return fib2(0, 1, 1)
