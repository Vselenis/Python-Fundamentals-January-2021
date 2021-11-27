single_string = input()
digits = []
letters = []
other = []
for el in single_string:
    if el.isdigit():
        digits.append(el)
    elif el.isalpha():
        letters.append(el)
    else:
        other.append(el)
print(''.join(digits))
print(''.join(letters))
print(''.join(other))