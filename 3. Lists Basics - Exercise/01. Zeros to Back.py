list_of_nums = input().split(', ')
nums = []
for num in list_of_nums:
    if num == '0':
        list_of_nums.append(0)
        pass
    else:
        nums.append(int(num))

print(nums)