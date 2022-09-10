# Find the sum of all the numbers that are equal to the sum of their digits to the fifth power
fpow = [i ** 5 for i in range(10)]
s = 0
for i in range(2, 350000):
    j = i
    n = 0
while j != 0:
    n += fpow[j % 10]
    j //= 10
 if (n == i): s += i
print("#30:", s)
