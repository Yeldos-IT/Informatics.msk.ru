s = set()
n = int(input())
for i in range(n):
    query = input().split()
    if query[0] == "ADD":
        s.add(int(query[1]))
    elif query[0] == "COUNT":
        print(len(s))
    elif query[0] == "PRESENT":
        print("YES" if int(query[1]) in s else "NO")