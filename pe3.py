def prime_factor2(n):
    divisor = 2
    num_store = 0
    while n > divisor:
        if n % divisor == 0:
            num_store = divisor
            n //= divisor
            divisor = 2
        else:
            divisor += 1
    return n
