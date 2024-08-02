n = int(input())
count = 0
i = 1
while n > 0:
    y = n
    x = ''
    while y > 0:
        x += str(y%10)
        y //= 10
    if n == int(x):
        count += 1
    n -= 1
print(count)