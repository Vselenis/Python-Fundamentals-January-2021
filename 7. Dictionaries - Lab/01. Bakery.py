list_of_strings = input().split()
dict = {}
for el in range(0, len(list_of_strings), 2):
    keys = list_of_strings[el]
    quantities = list_of_strings[el + 1]
    dict[keys] = int(quantities)
print(dict)
