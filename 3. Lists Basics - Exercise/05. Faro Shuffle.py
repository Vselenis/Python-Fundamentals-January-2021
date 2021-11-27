carts = input().split()
n = int(input())

half = int(len(carts) // 2)
result = []

for i in range(n):
    result = []
    for i in range(len(carts)):
        if i == len(carts) / 2:
            break
        one = carts[i]
        ff = i + half
        two = carts[ff]

        result.append(one)
        result.append(two)

    carts = result
print(result)
