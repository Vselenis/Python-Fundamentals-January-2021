def orders(product, num):
    result = 0
    if product == 'coffee':
        result += num * 1.5
    if product == 'water':
        result += num * 1
    if product == 'coke':
        result += num * 1.4
    if product == 'snacks':
        result += num * 2
    return result
product = input()
num = int(input())
print(f'{orders(product,num):.2f}')