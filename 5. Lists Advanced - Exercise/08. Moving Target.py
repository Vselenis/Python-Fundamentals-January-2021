moving_target = input().split()
moving_target = list(map(int, moving_target))
data = input()

def shoot(nums, i, v):
    if 0 <= i < len(nums):
        nums[i] -= v
        if nums[i] <= 0:
            nums.pop(i)
    return nums

def add_target(nums, i, v):
    if 0 <= i < len(nums):
        nums.insert(i, v)
    else:
        print('Invalid placement!')
    return nums

def strike(nums, i, v):
    left = i - v
    right = i + v
    if left >= 0 and right < len(nums):
        left = nums[:left]
        right = nums[right+1:]
        nums = left + right
    else:
        print('Strike missed!')
    return nums



while data != 'End':
    command, index, value = data.split()
    index = int(index)
    value = int(value)
    if command == 'Shoot':
        moving_target = shoot(moving_target, index, value)
    elif command == 'Add':
        moving_target = add_target(moving_target, index, value)
    elif command == 'Strike':
        moving_target = strike(moving_target, index, value)


    data = input()

print('|'.join(map(str, moving_target)))