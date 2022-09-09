# Find the number of distinct combinations of coins that add up to 2 pounds (200)
coins = [1, 2, 5, 10, 20, 50, 100, 200]
money = [[not(i or j) for j in range(len(coins))] for i in range(n + 1)]
for i in range(n + 1):
    for j in range(len(coins)):
        if i - coins[j] >= 0:
            money[i][j] = sum(money[i - coins[j]][:j + 1])
print("#31:", sum(money[-1]))
