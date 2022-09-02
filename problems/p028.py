# Find the sum of the diagonals of a number spiral. For example:
# 21 22 23 24 25
# 20 07 08 09 10
# 19 06 01 02 11
# 18 05 04 03 12
# 17 16 15 14 13
# Sum = 101

ls = [4] # stores the sum of the corners of the smaller spirals
def corner_sum(n):
    ind = int((n - 1) / 2)
    if ind < len(ls): return ls[ind]
    ls.append((ans := corner_sum(n - 2) + 16 * n - 28)) # formula I found for sum of corners of a bigger square in the spiral
    return ans
corner_sum(1001)
print("#28:", sum(ls) - 3) # the 1 in the center is counted 4 times in each diagonal
