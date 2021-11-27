import math
numbers = list(map(int, input().split(", ")))
max_num = max(numbers)
n = math.ceil(max_num / 10)

for i in range(1, n + 1):
    list_nums = []
    for num in numbers:
        if (i * 10) - 10 < num <= i * 10:

            list_nums.append(num)
    print(f"Group of {i * 10}'s: {list_nums}")
