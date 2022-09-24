# Find the last 10 digits of the sum of x^x up to x = 1000
n = 1000
def npow(n, x):
    if x <= 1: return (n ** x) % 10000000000
    if x % 2 == 0: return (npow(n, x // 2) ** 2) % 10000000000        
    else: return (n * (npow(n, x // 2) ** 2)) % 10000000000
print("#48:", sum((npow(x, x) for x in range(1, n))) % 10000000000)  
