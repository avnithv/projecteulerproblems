# Sum of even fibonacci numbers less than 4 million
ls = []
a, b = 1, 2
while b <= 4000000:
    if b % 2 == 0: 
        ls.append(b)
    a, b = b, b + a
print("#2:", sum(ls))
