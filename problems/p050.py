n = 1000000
seeve = [True for i in range(n)]
s = [0]
p = set()
for i in range(2, n):
    if seeve[i]:
        s.append(s[-1] + i)
        p.add(i)
        for v in range(i, n, i):
            seeve[v] = False
mp = 953
for i in range(len(s) - 1, 0, -1):
    j = 0
    while j < i:
        if (d := s[i] - s[j]) in p:
            mp = max(mp, d)
        if d < mp: j = i
print("#50:", mp)
