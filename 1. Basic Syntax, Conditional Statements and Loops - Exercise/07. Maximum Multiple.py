divisior = int(input())
bound = int(input())

for num in range(bound, 0 , -1):
    if num % divisior == 0:
        print(num)
        break