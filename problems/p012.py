# Find the first triangluar number with more than 500 factors
tnum = lambda n : int(n * (n + 1) / 2) # formula for triangular numbers
def div(n, s = 2): # number of factors is the product of one plus all of the exponents in the prime factorization
    ndiv = 1
    while s <= n // 2:
        p = 1
        while n % s == 0: 
            p += 1
            n = int(n / s)
        ndiv *= p
        s += 1
    if n > 1: ndiv *= 2 
    return ndiv

term = 1
num = tnum(term)
while div(num) <= 500:
    term += 1
    num = tnum(term)
print("#12:", num)
