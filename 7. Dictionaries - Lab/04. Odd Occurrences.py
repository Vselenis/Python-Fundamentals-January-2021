words = input().split()

lang = {}
words = [w.lower() for w in words]

for word in words:
    lang[word] = words.count(word)

for key, value in lang.items():
    if value % 2 != 0:
        print(key, end=' ')
