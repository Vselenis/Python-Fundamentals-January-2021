n = int(input())
sum = 0
for _ in range(n):
    chr = input()
    sum += ord(chr)
print(f'The sum equals: {sum}')