M, N = map(int, input().split())
x, y = map(int, input().split())

# Выводим соседей в заданном порядке
if y > 1:
    print(x, y - 1)
if x > 1:
    print(x - 1, y)
if y < N:
    print(x, y + 1)
if x < M:
    print(x + 1, y)