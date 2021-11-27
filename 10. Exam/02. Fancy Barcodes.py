import re

n = int(input())
pattern = r'@+#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@+#+'

for _ in range(n):
    text = input()
    matches = re.match(pattern, text)
    if matches == None:
        print('Invalid barcode')
        continue
    find_digits = []
    for symbol in matches.group(1):
        if symbol.isdigit():
            find_digits += symbol
        else:
            pass

    if len(find_digits) == 0:
        print('Product group: 00')
    else:
        print(f"Product group: {''.join(find_digits)}")