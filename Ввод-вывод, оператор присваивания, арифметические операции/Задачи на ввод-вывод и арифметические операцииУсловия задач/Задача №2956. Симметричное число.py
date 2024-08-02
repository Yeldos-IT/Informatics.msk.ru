n = int(input())
a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10
e = (a == d) * (b == c)
print((e == 1) - 37 * (e != 1))