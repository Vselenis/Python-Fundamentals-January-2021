n = int(input())
sum_liters = 0

for i in range(n):

    liters = int(input())
    sum_liters += liters

    if sum_liters <= 255:
        continue
    else:
        sum_liters -= liters
        print("Insufficient capacity!")
print(sum_liters)