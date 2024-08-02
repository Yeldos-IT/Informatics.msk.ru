a = 1
count = 0
summ = 0
while a != 0:
    x = int(input())
    if x == 0:
        break
    if x % 2 == 0:
        count += 1

print(count)