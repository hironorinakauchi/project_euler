def sum_square(upto):
    total = 0
    for i in range(1, upto+1):
        total += i*i
    return total

def square_sum(upto):
    total = 0
    for i in range(1, upto + 1):
        total += i
    return total**2

print(square_sum(100) - sum_square(100))
