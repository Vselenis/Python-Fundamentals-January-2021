n = int(input())
positive = []
negative = []
sumirane = 0
for index in range(n):
    number = int(input())
    if number > 0:
        positive.append(number)
    else:
        negative.append(number)
        sumirane += number
print(positive)
print(negative)
print(f'Count of positives: {len(positive)}. Sum of negatives: {sumirane}')