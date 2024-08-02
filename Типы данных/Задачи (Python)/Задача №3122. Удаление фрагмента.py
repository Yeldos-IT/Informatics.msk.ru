words=input()
words=words[:words.find('h')] + words[words.rfind('h') + 1:]
print(words)