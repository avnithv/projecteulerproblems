# Find the number of numbers less than 10 million that reach 89 if you repeatedly sum the square of their digits
ls = [0 for i in range(n)]
ls[1] = 1
ls[89] = 89
s = 0
for i in range(1, n):
    if not ls[i]:
        l = [i]
        while not ls[l[-1]] and ls[l[-1]] != 89 and ls[l[-1]] != 1:
            l.append(sum([int(ch) ** 2 for ch in str(l[-1])]))
            r = ls[l[-1]]
            while l:
                k = l.pop()
                ls[k] = r
            if ls[i] == 89: s += 1
print("#92:", s)
