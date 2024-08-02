def isPalindrom(text):

    string = ''

    for i in  text:
        string += i
    if string == string[::-1]:
        return 'yes'
    else:
        return 'no'

s = input().split()

print(isPalindrom(s))