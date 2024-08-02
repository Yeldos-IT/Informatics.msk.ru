k, n = map(int, input().split())
page = (n + k - 1) // k
line_on_page = (n - 1) % k + 1
print(page, line_on_page)