# Find the sum of all the prime numbers less than 2 million
upperlim = 2000000
seeve = [True for i in range(upperlim)]
s = 0
for i in range(2, upperlim):
    if seeve[i]:
        s += i
        for v in range(i, upperlim, i):
            seeve[v] = False
print("#10:", s)
