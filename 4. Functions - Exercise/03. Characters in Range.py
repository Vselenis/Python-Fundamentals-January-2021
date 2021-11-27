def get_characters_between(start, end):
    for symbol in range(ord(start) + 1, ord(end)):
        res = ''
        res = symbol
        print(chr(res), end = ' ')
start = input()
end = input()
res = get_characters_between(start, end)
