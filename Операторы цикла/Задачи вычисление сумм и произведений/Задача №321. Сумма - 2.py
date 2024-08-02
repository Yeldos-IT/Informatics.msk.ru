n = int(input())
r = 0
for i in range(n + 1):
    r += (-1) ** i / (2 * i + 1)
r *= 4
print(r)