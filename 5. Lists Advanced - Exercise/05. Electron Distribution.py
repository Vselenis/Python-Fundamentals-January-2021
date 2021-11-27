my_number = int(input())
sum_of_nums = []
n = 1
while my_number > 0:
    nums = 2*n**2
    n += 1
    if my_number > nums:
        sum_of_nums.append(nums)
        my_number -= nums
    else:
        sum_of_nums.append(my_number)
        break
print(sum_of_nums)