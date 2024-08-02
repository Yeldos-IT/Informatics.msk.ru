n = int(input())
minimum = n%10
maximum = -1
while n > 0:
    x = n%10
    if x > maximum:
        maximum = x
    if x < minimum:
        minimum = x
    n //= 10
print(minimum, maximum)