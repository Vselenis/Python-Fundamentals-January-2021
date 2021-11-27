nums = input().split(', ')
n = int(input())
numbers = []
beggars = []
for nums_str in nums:
    number = int(nums_str)
    numbers.append(number)
for i in range(n):
    beggars.append(0)
index = 0
for number in numbers:
    beggars[index] += number
    index += 1

    if index == n:
        index = 0
print(beggars)

