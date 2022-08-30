# Find the largest prime factor of n
n = 600851475143
factors = []
i = 2
while n != 1:
    if n % i == 0:
        factors.append(i)
        n /= i
    else: 
        i += 1
print("#3:", max(factors))
