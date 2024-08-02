a = int(input())
b = int(input())
c = (b % a > 0) * ((b // a + 1) * a - b)
print(c)