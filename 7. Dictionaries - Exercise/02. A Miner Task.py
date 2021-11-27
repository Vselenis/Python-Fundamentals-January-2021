metal = input()
dict = {}

while metal != 'stop':
    quantity = int(input())

    if metal in dict:
        dict[metal] += quantity
    else:
        dict[metal] = quantity

    metal = input()

for key, value in dict.items():
    print(f'{key} -> {value}')