x = 1
y = 0
for i in range(1, int(input())+1):
    y += 1
    print(x, end=' ')
    if x == y:
        x += 1
        y = 0