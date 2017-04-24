def prime_generator(limit):
    prime_lst = [True]*limit
    prime_lst[0] = prime_lst[1] = False
    
    for (i, is_prime) in enumerate(prime_lst):
        if is_prime:
            yield i
            for n in range(i*i, limit, i):
                prime_lst[n] = False

lst = []
for i in prime_generator(2000000):
    lst.append(i)
print(sum(lst))
