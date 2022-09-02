# Find the longest Collatz Sequence with a starting number of less than 1 million
coll = lambda x : 3 * x + 1 if x % 2 else int(x / 2)
coll_len = {1:1} # stores previously calculated values for fast lookup

maxi = 1
for i in range(2, 1000000):
    st = 0
    num = i
    while num not in coll_len:
        num = coll(num)
        st += 1
    coll_len[i] = st + coll_len[num]

    if coll_len[i] > coll_len[maxi]: maxi = i
print("#14:", maxi)
