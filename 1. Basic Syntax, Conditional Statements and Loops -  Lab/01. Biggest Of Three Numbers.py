import sys


minimal = - sys.maxsize

for num in range(0, 3):
    number = int(input())
    if number > minimal:
        minimal = number

print(minimal)