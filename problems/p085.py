# Find the area of the rectangular grid where the number of rectangles inside the grid with corners on lattice points is closest to 2 million
n = 2000000
zz = lambda x: ((x + 1) * x) // 2
s = floor(n ** 0.25)
ab = None
d = 1000000000
dc = {}
print(s)
for i in range(s - 100, s + 100):
    for j in range(s - 100, s + 100):
    if i <= 0 or j <= 0: continue
    if j not in dc: dc[j] = zz(j)
    if abs(zz(i) * zz(j) - n) < d:
        d = abs(zz(i) * zz(j) - n)
        ab = (i, j)
print("#85:", ab[0] * ab[1])
