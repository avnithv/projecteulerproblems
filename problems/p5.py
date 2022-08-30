# Find the LCM of the numbers from 1-20
n = 20
def highest_power(n, a): # highest power of a less than n
    ans = 1
    while n >= ans: ans *= a
    return ans / a

ans = 1
for i in range(2, n):
    if ans % i == 0: continue # always goes into this branch if composite
    ans *= int(highest_power(n, i))
