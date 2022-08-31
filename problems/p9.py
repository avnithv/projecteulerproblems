# Find the sides of a right triangle a, b, c where a + b + c = 1000 
ans = None
for a in range(1, 999):
    for b in range(a, 999):
        c = 1000 - a - b
        if (pow(a, 2) + pow(b, 2) + pow(c, 2) - 2 * (pow(max(a, b, c), 2))) == 0: # pythagorean theorem but cooler
            ans = (a, b, 1000 - a - b)
            break
    if ans: break
print("#9:", ans[0] * ans[1] * ans[2])
