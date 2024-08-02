def countOfWords(text):

    l = []

    words = []
    for i in text:
        l.append(len(i))
        words.append(i)
    return words[l.index(max(l))], max(l)

s = input().split()
print(*countOfWords(s), sep='\n')