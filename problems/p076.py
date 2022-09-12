# Number of distinct ways to sum up to N using natural numbers <N
nums = [i for i in range(1, n)]
totals = [[(i <= 2 and not j) for j in range(len(nums))] for i in range(n + 1)]
for i in range(n + 1):
    for j in range(len(nums)):
        if i - nums[j] >= 0:
            totals[i][j] = sum(totals[i - nums[j]][:j + 1])
print("#76:", sum(totals[-1]))
