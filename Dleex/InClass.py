"""List breaking"""

x = [10, 25, 48]

l = []

for i in x:
    while i >= 10:
        g = i % 10
        i //= 10
        g = i % 10
        l.append(g)
        i //= 10
    while i != 0:
        g = i % 10
        l.append(g)
        i //= 10
print(l)
