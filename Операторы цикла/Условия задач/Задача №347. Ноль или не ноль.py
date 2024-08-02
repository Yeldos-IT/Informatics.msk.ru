N = int(input())
has_zero = False
for _ in range(N):
    num = int(input())
    if num == 0:
        has_zero = True
        break
if has_zero:
    print("YES")
else:
    print("NO")