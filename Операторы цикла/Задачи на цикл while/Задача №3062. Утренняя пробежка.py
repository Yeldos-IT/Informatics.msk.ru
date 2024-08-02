x = int(input())
y = int(input())

count = 1
while y > x:
    count += 1
    x += x * 0.1

print(count)