# Find the number of letters in the numbers from 1 to 1000 inclusive
ones, tens, teens, hundred, sm = (0, 3, 3, 5, 4, 4, 3, 5, 5, 4), (0, 3, 6, 6, 5, 5, 5, 7, 6, 6), (3, 6, 6, 8, 8, 7, 7, 9, 8, 8), 7, 0
for i in range(1, n):
    if i >= 100: sm += ones[i // 100] + hundred + (3 if i % 100 else 0)
    if 10 <= i % 100 < 20: sm += teens[(i % 100) - 10]
    else: sm += tens[(i % 100) // 10] + ones[i % 10]
print("#17:", sm + 11)
