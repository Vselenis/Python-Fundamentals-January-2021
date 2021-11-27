quantities_dict = {}
prices_dict = {}
while True:
    product_info = input()

    if product_info == 'buy':
        break
    (product, price1, quantity1) = product_info.split(' ')
    price = float(price1)
    quantity = int(quantity1)
    prices_dict[product] = price
    if product not in quantities_dict:
        quantities_dict[product] = 0
    quantities_dict[product] += quantity

for (key,price) in prices_dict.items():
    total_sum = price * quantities_dict[key]
    print(f'{key} -> {total_sum:.2f}')
