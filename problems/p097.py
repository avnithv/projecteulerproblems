# Find the last 10 digits of 2^7830457 * 28433 + 1
def npow(n, x):
    if x <= 1: return (n ** x) % 10000000000
    if x % 2 == 0: return (npow(n, x // 2) ** 2) % 10000000000        
    else: return (n * (npow(n, x // 2) ** 2)) % 10000000000
print("#97:", (npow(2, 7830457) * 28433 + 1) % 10000000000)   
