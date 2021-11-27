n = int(input())
even_num = []
odd_num = []
negative = []
positive = []

for i in range(n):
    number = int(input())
    if number % 2 == 0:
        even_num.append(number)
    if number % 2 == 1:
        odd_num.append(number)
    if number >= 0:
        positive.append(number)
    if number < 0:
        negative. append(number)

spec = input()
if spec == 'even':
    print(even_num)
elif spec == 'odd':
    print(odd_num)
elif spec == 'positive':
    print(positive)
elif spec == 'negative':
    print(negative)