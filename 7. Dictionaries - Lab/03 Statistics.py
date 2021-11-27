food = input()

dict = {}

while food != 'statistics':
    product, quantities = food.split(': ')
    quantities = int(quantities)
    if product in dict:
        dict[product] += quantities
    else:
        dict[product] = quantities
    food = input()
print('Products in stock:')
for key, value in dict.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(dict)}')
print(f'Total Quantity: {sum(dict.values())}')