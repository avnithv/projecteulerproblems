# Find the 10001st prime number
def is_prime(n):
    if n == 2: return True
    if n % 2 == 0: 
        return False
    for i in range(3, round(pow(n, 0.5) + 1), 2):
        if n % i == 0: 
            return False
    return True

count = 0
x = 2
while count < 10000:
    if is_prime(x): count += 1
    x += 1
print("#7:", x - 1)
