# Find the path from the top to the bottom of the triangle with the maximum sum (see problem 018(
for i in range(len(data) - 2, -1, -1):
    for j in range(i + 1):
        data[i][j] += max(data[i + 1][j], data[i + 1][j + 1])
print("#67:", data[0][0])
