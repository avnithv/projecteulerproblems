n = 5000
upperlim = 100000
seeve = [True for i in range(upperlim)]
nums = []
for i in range(2, upperlim):
    if seeve[i]:
        nums.append(i)
        for v in range(i, upperlim, i):
            seeve[v] = False
totals = [[(i <= 2 and not j) for j in range(len(nums))] for i in range(upperlim)]
ans = -1
for i in range(upperlim):
    for j in range(len(nums)):
        if i - nums[j] >= 0:
            totals[i][j] = sum(totals[i - nums[j]][:j + 1])
        if totals[i][-1] > n:
            ans = i
            break
print("#77:", ans)
