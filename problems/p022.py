# Find the sum of the letter score times the position of the name in alphabetical order
data = []
alph = {chr(x + 64) : x for x in range(1, 27)}
print("#22:", sum(((sum(map(lambda x : alph[x], list(v))) * (i + 1) for i, v in enumerate(sorted(data))))))
