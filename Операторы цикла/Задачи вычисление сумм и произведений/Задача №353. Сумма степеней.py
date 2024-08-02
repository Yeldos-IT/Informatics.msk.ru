n = int(input())
r = 0

for i in range(n + 1):
    r += 2 ** i

print(r)