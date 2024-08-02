a = int(input())

if (a % 10 > 1) and (a % 10 < 5) and ((a // 10 % 10) != 1):
    print(f'{a} bochki')
elif ((a // 10 % 10) != 1) and (a % 10 == 1):
    print(f'{a} bochka')
else:
    print(f'{a} bochek')