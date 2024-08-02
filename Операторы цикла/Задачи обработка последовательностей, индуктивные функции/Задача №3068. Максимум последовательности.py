a = 1
max = -1
while a != 0:
    x = int(input())
    if x == 0:
        break
    if x > max:
        max = x

print(max)