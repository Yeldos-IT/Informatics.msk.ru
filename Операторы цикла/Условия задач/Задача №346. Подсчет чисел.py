zeroCount = 0
positiveCount = 0
negativeCount = 0

for i in range(int(input())):

    n = int(input())
    if n == 0:
        zeroCount += 1
    if n > 0:
        positiveCount += 1
    if n < 0:
        negativeCount += 1


print(zeroCount, positiveCount, negativeCount)