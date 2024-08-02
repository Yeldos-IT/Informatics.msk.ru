max = int(input())
max2 = int(input())
if max2 > max:
    max, max2 = max2, max
x = int(input())
while x != 0:
    if x > max:
        max2, max = max, x
    elif x > max2:
        max2 = x
    x = int(input())
print(max2)