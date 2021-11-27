word = input().split()
for el in word:
    combo = el*len(el)
    print(f'{combo}', end = '')