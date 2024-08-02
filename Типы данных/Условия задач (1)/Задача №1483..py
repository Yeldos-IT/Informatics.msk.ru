hours, minutes, seconds = map(int, input().split())
hours1, minutes1, seconds1 = map(int, input().split())
seconds_1 = ((hours * 60) * 60) + (minutes * 60) + seconds
seconds_2 = ((hours1 * 60) * 60) + (minutes1 * 60) + seconds1
result = seconds_2 - seconds_1
print(result)