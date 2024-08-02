n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    count = 1
    while b <= n:
        if b == n:
            print(count)
            break
        a, b = b, a + b
        count += 1
    else:
        print(-1)