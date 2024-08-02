n = int(input())
print(str(n % 86400 // 3600) + ':' + str(n % 3600 // 60 // 10) + str(n % 3600 // 60 % 10) + ':' + str(n % 60 // 10) + str(n % 10))