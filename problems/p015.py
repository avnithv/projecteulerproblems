# Find the number of lattice paths in a 20x20 grid
a = b = 20
def fact(n):
    if n <= 1: return 1
    return n * fact(n - 1)
print("#15:", int(fact(a + b) / (fact(a) * fact(b))))
