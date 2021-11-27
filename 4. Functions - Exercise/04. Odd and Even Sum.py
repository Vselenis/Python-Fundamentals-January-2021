
def get_odd_even_sum(string):
    odd = 0
    even = 0
    for el in string:
        num = int(el)
        if num % 2 == 1:
            odd += num
        else:
            even += num
    print(f'Odd sum = {odd}, Even sum = {even}')

string = input()
output = get_odd_even_sum(string)
