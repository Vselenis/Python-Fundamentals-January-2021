text = input()
result = ''
i = 0
n = 0
while i < len(text):
    if text[i] == '>':
        result += '>'
        i += 1
        n += int(text[i])
        while n > 0 and text[i] != '>':
            i += 1
            n -= 1
            if i >= len(text):
                break
    else:
        result += text[i]
        i += 1

print(result)