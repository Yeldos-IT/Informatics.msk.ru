n = int(input())
k = int(input())
n1 = 1
k1 = 1
m = 1

for i in range(1, n + 1):
    n1 *= i

for i in range(1, k + 1):
    k1 *= i

for i in range(1, (n - k) + 1):
    m *= i

result = n1 // (k1 * m)
print(result)