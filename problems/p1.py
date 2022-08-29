# Sum of all multiples of 3 or 5 less than 1000
print("#1:", sum([x if (x % 3 == 0 or x % 5 == 0) else 0 for x in range(1000)]))
