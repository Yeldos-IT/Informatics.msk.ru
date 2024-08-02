a = input().split()
b = set()
for c in a:
    if c in b:
        print('YES')
    else:
        print('NO')
    b.add(c)