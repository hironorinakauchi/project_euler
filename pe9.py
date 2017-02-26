def find_abc():
    for a in range(1, 1001):
        for b in range(a + 1, a + 1001):
            if a + b > 1000:
                break
            c = 1000 - (a + b)

            if a**2 + b**2 == c**2:
                return a*b*c

ans = find_abc()

def euler9():
    for c in range(2, 1000):
        for b in range(1, c):
            a = 1000 - c - b

            if a**2 + b**2 == c**2:
                print("a = %d, b = %d, c = %d, abc = %d" %(a, b, c, a*b*c))
                return
euler9()
