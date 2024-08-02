a = float(input())
b = float(input())
c = float(input())
if a + b == c:
    print("YES")
elif round(a + b, 7) == round(c, 7):
    print("YES")
else:
    print("NO")