# Find the largest product of 2 three digit numbers that is a palindrome
ans = -1
for a in range(999, 100, -1):
    for b in range(999, a - 1, -1):
        prod = str(a * b)
        # checks if product is palindrome by reversing it
        if prod == prod[::-1] and int(prod) > ans: 
            ans = int(prod)
print("#4:", ans)
