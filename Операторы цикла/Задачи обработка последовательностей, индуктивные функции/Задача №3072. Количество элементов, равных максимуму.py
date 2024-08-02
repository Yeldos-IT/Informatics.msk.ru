max = int(input())
count = 1
x = int(input())
while x != 0:
    if x == max:
        count += 1
    if x > max:
        max = x
        count = 1
    x = int(input())
print(count)