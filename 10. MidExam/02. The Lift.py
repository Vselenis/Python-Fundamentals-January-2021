queue = int(input())
nums_of_lifts = [int(x) for x in input().split()]
for i in range(len(nums_of_lifts)):
    free_space = 4 - nums_of_lifts[i]

    if queue > free_space:
        nums_of_lifts[i] += free_space
        queue -= free_space
    elif queue == free_space:
        nums_of_lifts[i] += queue
        queue = 0
        break
    else:
        nums_of_lifts[i] += queue
        queue = 0
        print('The lift has empty spots!')
        break

if queue > 0:
    print(f"There isn't enough space! {queue} people in a queue!")
print(' '.join(str(x) for x in nums_of_lifts))