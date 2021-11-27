def parse_to_char(word):
    temp = ''
    for char in word:
        if not str(char).isdigit():
            break
        temp += char
    ascii_value = int(temp)
    char_value = chr(ascii_value)
    new_word = word.replace(temp, char_value)
    return new_word

def replace_in_word(word):
    temp = list(word)
    temp[1], temp[-1] = temp[-1], temp[1]
    return ''.join(temp)

def decrypt(word):
    result = parse_to_char(word)
    result = replace_in_word(result)
    return result

words = input().split()
new_words = [decrypt(word) for word in words]
print(' '.join(new_words))
