def is_palindrom(element):
    reversed_element = element[::-1]
    if element == reversed_element:
        return True
    return False

def separate_elemnts(text, sep):
    number_as_string = text.split(sep)
    return number_as_string

data = input()
num_strings = separate_elemnts(data, ', ')

for el in num_strings:
    print(is_palindrom(el))