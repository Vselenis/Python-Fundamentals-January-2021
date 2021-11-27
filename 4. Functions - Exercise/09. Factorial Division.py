def fakturiel_num(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result
number_one = int(input())
number_two = int(input())

fakturiel_one = fakturiel_num(number_one)
fakturiel_two = fakturiel_num(number_two)

end = fakturiel_one / fakturiel_two
print(f'{end:.2f}')