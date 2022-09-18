# Find the sum of the digits of 100!
f = 1
for i in range(1, 100): f *= i
print("#22:", sum(map(int, list(str(f)))))
